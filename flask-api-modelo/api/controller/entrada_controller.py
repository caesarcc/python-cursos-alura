from api.library import api_helper as Helper
from flask import render_template

class EntradaController:

    def index(self):
        return Helper.response(200, "Bem vindo ao serviço de APIs do Cidadão RS")

    def home(self):
        return render_template('bemvindo.html')