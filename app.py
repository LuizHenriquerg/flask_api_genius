from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(str(Path(__file__).parent.absolute()) + '/.env')

app = Flask(__name__)