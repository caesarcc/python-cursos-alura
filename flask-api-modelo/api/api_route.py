from api import api
from api.controller.entrada_controller import EntradaController

# Router Basic #
@api.route("/api/", methods=["GET"])
def entrada():
    return EntradaController().index()
