from http import HTTPStatus
from flask import Blueprint, json, request
from flasgger import swag_from
from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

import requests

dealer_api = Blueprint('dealer', __name__)

@dealer_api.route('/new', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Valor do Dealer'
        }
    }
})

def dealer():
    """
    Seja bem vindo
    API do desafio Backend do O Boticario
    ---
    """
    db = get_db()
    error = None

    try:
        db.execute(
        '''INSERT INTO dealer (fullname, password, cpf, email)
            VALUES (?, ?, ?, ?)''', ('Maria Maria', generate_password_hash('password'), '12312312323', 'maria@gmail.com')
        )
    except Exception as e:
        print(e)
        return 'Error'
    else:
        db.commit()

    return 'Feito', 200

@dealer_api.route('/valid', methods=['POST'])
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
    payload = request.args


    db = get_db()
    error = None

    try:
        retorno = db.execute(
        'SELECT cpf, password FROM dealer where cpf = ?;', (payload['cpf'],)
        ).fetchone()
    except Exception as e:
        print(e)
    else:
        if retorno is None:
            print('nao achei ninguem')
            return 'nao encontrado'
        else:
            if check_password_hash(retorno['password'], payload['password']):
                token = create_access_token(identity=payload['cpf'])
                return {'token': token}

    return 'Deu algum erro', 200



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