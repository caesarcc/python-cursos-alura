from werkzeug.routing import PathConverter
from api import api
from api.library import api_helper as Helper
from flask_cors import CORS

cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

# Converter Url
class EverythingConverter(PathConverter):
    regex = '.*?'

api.url_map.converters['everything'] = EverythingConverter
# END converter

# Router Error #
@api.errorhandler(400)
def bad_request(error):
    return Helper.response(400, "Requisição não foi recebida devido à sintaxe incorreta."), 400

@api.errorhandler(405)
def method_not_allowed(error):
    return Helper.response(405, "O método enviado não é permitido para esta URL."), 405

@api.errorhandler(404)
def page_not_found(error):
    return Helper.response(404, "URL solicitada não foi encontrada."), 400

@api.errorhandler(403)
def forbidden_error(error):
    return Helper.response(403, "Solicitão reconhecida mas não autorizada."), 403

@api.errorhandler(500)
def internal_server_error(error):
    return Helper.response(500, "Erro interno do servidor."), 500
# End Router Error #
