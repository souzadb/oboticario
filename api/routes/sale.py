from http import HTTPStatus
from flask import Blueprint, json
from flasgger import swag_from

sale_api = Blueprint('sale', __name__)

@sale_api.route('/new', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'New Sale',
            'schema' : SaleSchema
        }
    }
})

def new_sale():
    """
    New Sale
    New sale by CPF
    ---
    """
    data = {
        'cod': 123,
        'value': 123,
        'date': 'today',
        'cpf': 'texto',
        'status': 'Validacao'
    }
    result = SaleModel(data)
    return SaleSchema().dump(result), 200

@sale_api.route('/sales', methods = ['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'All Dealer Sales',
        }
    }
})

def all_sales():
    """
    All Dealer Sales
    ---
    ---
    """
    data = {
        'cod': 123,
        'value': 123,
        'date': 'today',
        'cpf': 'texto',
        'status': 'Validacao'
    }
    result = json.dumps(data)
    result = json.loads(result)
    return result, 200