from flask import Flask
from src.config.routes import blueprint_urls
from src.config.db import initialize_db
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://127.0.0.1:27017/boilerplate-db-flask'
}

initialize_db(app)

app.register_blueprint(blueprint_urls)