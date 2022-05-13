from flask import jsonify
import requests
from utils.database import Dynamo
import redis
import os
import json 
from uuid import uuid4

class Musica:
    def __init__(self):
        db = Dynamo()
        self.db = db.database()
        
        self.redis_cliente = redis.Redis(
            host=os.environ.get('REDIS_HOST'),
            port=os.environ.get('REDIS_PORT')
        )
    
    def genius(self, artista):
        url = os.environ.get('GENIUS_BASE_URL') + f'search/?q={artista}'
        token_acesso = os.environ.get('GENIUS_ACCESS')

        response_req = requests.get(
            url=url,
            data={
                'access_token': token_acesso
            }
        )

        response = response_req.json()

        if response_req.status_code == 200 and 'response' in response:
            return response['response']['hits']
        
        return None
    
    def musicas(self, artista, cache=True):
        if cache is None or bool(cache):
            response = self.redis_cliente.get(artista)

            if response is not None:
                response = response.decode('utf-8')
                response = json.loads(str(response).replace("'", '"'))

                return response
        
        musicas_response = self.genius(artista)

        if musicas_response is None or len(musicas_response) == 0:
            return None

        musicas_list = []
        
        for i in musicas_response:
            musicas_list.append({
                'titulo': i['result']['title'],
                'artistas': i['result']['artist_names']
            })
        
        self.db.put_item(
            Item={
                'nome': artista,
                'musicas': musicas_list
            }
        )

        doc_artista = {
            'Id': str(uuid4()),
            'artista': artista,
            'musicas': musicas_list
        }

        doc_response = {
            'status': 'sucesso',
            'data': doc_artista
        }

        self.redis_cliente.delete(artista)
        self.redis_cliente.set(artista, str(doc_response))
        self.redis_cliente.expire(artista, 604800)

        return doc_response
