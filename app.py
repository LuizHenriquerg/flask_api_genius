from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(str(Path(__file__).parent.absolute()) + '/.env')

app = Flask(__name__)

from controllers.artista import artista_rota
app.register_blueprint(artista_rota, url_prefix='/api/v1/captura')