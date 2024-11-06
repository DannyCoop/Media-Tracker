from flask import Flask
from app.routes import user, media
import firebase_admin
import fireo
from firebase_admin import credentials
from app.settings import (
    GOOGLE_CREDENTIALS,
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.register_blueprint(user.blueprint, url_prefix="/user")
app.register_blueprint(media.blueprint, url_prefix="/media")

creds = credentials.Certificate(GOOGLE_CREDENTIALS)
firebase_admin.initialize_app(creds)
fireo.connection(from_file=GOOGLE_CREDENTIALS)

app.run(port=8080)