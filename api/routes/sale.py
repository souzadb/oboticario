from http import HTTPStatus
from flask import Blueprint, json, request, app
from flasgger import swag_from
from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity


sale_api = Blueprint('sale', __name__)


@sale_api.route('/new', methods=['POST'])
@jwt_required
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'New Sale'
        }
    }
})

def new_sale():
    """
    New Sale
    New sale by CPF
    ---
    """
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')

    payload = request.args
    token = request.headers.get('token')
    print(payload, token)

    db = get_db()
    error = None

    try:
        db.execute(
        '''INSERT INTO sale (cod, value, date, cpf)
            VALUES (?, ?, ?, ?)''', (payload['cod'], payload['value'], payload['date'], payload['cpf'])
    )
    except Exception as e:
        return 'Something was wrong, {0}'.format(e), 400
    else:
        db.commit()

    result = json.dumps(payload)
    result = json.loads(result)
    return result, 200

@sale_api.route('/sales', methods=['GET'])
@jwt_required
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
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')

    db = get_db()
    error = None

    retorno = db.execute(
        'SELECT * FROM sale WHERE cpf = "12312312323"'
    ).fetchall()

    retorno = [list(x) for x in retorno]
    print(retorno)

    retorno = json.dumps(retorno)
    retorno = json.loads(retorno)
    print(retorno)
    return retorno, 200