from api import api
from api.controller.entrada_controller import EntradaController

@api.route('/')
def home():
    return EntradaController().home()
    