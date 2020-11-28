from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.models.sale import NewSaleModel
from api.schemas.sale import NewSaleSchema

sale_api = Blueprint('sale', __name__)

@sale_api.route('/new')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'New Sale',
            'schema' : NewSaleSchema
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
    result = NewSaleModel(data)
    return NewSaleSchema().dump(result), 200