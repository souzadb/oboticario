from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.models.dealer import DealerModel, VendaModel
from api.schemas.dealer import DealerSchema, VendaSchema

dealer_api = Blueprint('dealer', __name__)

@dealer_api.route('/dealer')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Valor do Dealer',
            'schema' : DealerSchema
        }
    }
})

def dealer():
    """
    Seja bem vindo
    API do desafio Backend do O Boticario
    ---
    """
    result = DealerModel()
    return DealerSchema().dump(result), 200


@dealer_api.route('/venda')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Foi vendido',
            'schema' : VendaSchema
        }
    }
})

def venda():
    """
    Seja bem vindo
    API do desafio Backend do O Boticario
    ---
    """
    result = VendaModel()
    return VendaSchema().dump(result), 200
