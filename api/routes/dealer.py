from http import HTTPStatus
from flask import Blueprint, json
from flasgger import swag_from
from api.models.dealer import DealerModel
from api.schemas.dealer import DealerSchema

import requests

dealer_api = Blueprint('dealer', __name__)

@dealer_api.route('/new', methods=['POST'])
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
    data = {}
    result = DealerModel(data)
    return DealerSchema().dump(result), 200

@dealer_api.route('/valid', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Dealer Valided'
        }
    }
})

def valid():
    """
    Validando Login
    ---
    ---
    """
    data = {
        'cpf': '12312312332',
        'password': 'password'
    }
    result = json.dumps(data)
    return result, 200



@dealer_api.route('/cashback', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Cashback Total'
        }
    }
})

def cashback():
    """
    Retorno de cashback
    ---
    ---
    """
    result = requests.get('https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323',
                            headers = {'token': 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'})
    result = json.loads(result.text)
    return result, 200