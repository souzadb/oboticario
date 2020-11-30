from http import HTTPStatus
from flask import Blueprint, json, request
from flasgger import swag_from
from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3


sale_api = Blueprint('sale', __name__)

@sale_api.route('/new', methods=['POST'])
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
    payload = request.args
    token = request.headers.get('token1')
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