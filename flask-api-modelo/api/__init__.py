from flask import Flask
api = Flask(__name__, template_folder='views')

from api import base_route
from api import api_route
from api import web_route
