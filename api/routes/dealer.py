from http import HTTPStatus
from flask import Blueprint, json
from flasgger import swag_from
from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

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

    db.execute(
        '''INSERT INTO dealer (fullname, password)
            VALUES (?, ?)''', ('Mobeka', generate_password_hash('password'))
    )
    db.commit()

    data = {
        'name': 'Maria Marcia',
        'cpf': '123112312323',
        'email': 'maria@gmail.com',
        'password': 'password'
    }
    result = json.dumps(data)
    result = json.loads(data)
    return result, 200

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
    db = get_db()
    error = None

    retorno = db.execute(
        'SELECT * FROM user'
    ).fetchall()
    
    if retorno is None:
        print('tabela vazia')
    else:
        print('tem algo aqui')
        for line in retorno:
            print(line, line[0], line[1], line[2])

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