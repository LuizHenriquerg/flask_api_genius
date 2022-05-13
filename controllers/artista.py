from models.musica import Musica
from flask.views import MethodView
from flask import jsonify, Blueprint, request

artista_rota = Blueprint('artista_rota', __name__)

class Artista(MethodView):

    def __init__(self):
        self.genius_musica = Musica()

    def post(self):
        nome_artista = request.form.get('nome_artista')
        cache = request.args.get('cache')

        if nome_artista is None or nome_artista == '':
            return jsonify({
                'status': 'erro',
                'mensagem': 'por favor, enviar um nome de artista valido.'
            })

        response = self.genius_musica.musicas(
            artista=nome_artista, 
            cache=cache
        )

        if response is None:
            return jsonify({
                'status': 'erro',
                'mensagem': 'houve um erro ao obter as informacoes do artista. Tente novemente.'
            })
        
        return jsonify(response)


artista_view = Artista.as_view('artista_view')
artista_rota.add_url_rule('/artista', view_func=artista_view, methods=['POST'])