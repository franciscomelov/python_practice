from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version="1.0",
    title="Horoscope API",
    description="Get horoscope data easily using the below APis",
    license="MIT",
    contact="Ashutosh Krishna",
    contact_url="123.com",
    contact_email="123@hotmail.com",
    doc="/",
    prefix="/api/1"
)
