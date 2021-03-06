from http import HTTPStatus
from flask import Blueprint, json, request, current_app
from flasgger import swag_from
from oboticario.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sqlite3 import IntegrityError

import requests

dealer_api = Blueprint('dealer', __name__)

@dealer_api.route('/new', methods=['POST'])
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
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')

    if not request.get_json():
        return 'No json was passed', 400

    payload = request.get_json()

    if not 'fullname' in payload.keys():
        return 'No name was passed', 400
    elif not 'password' in payload.keys():
        return 'No password was passed', 400
    elif not 'cpf' in payload.keys():
        return 'No cpf was passed', 400
    elif not 'email' in payload.keys():
        return 'No email was passed', 400
    else:
        db = get_db()
        try:
            db.execute(
            '''INSERT INTO dealer (fullname, password, cpf, email)
                VALUES (?, ?, ?, ?)''', (payload['fullname'], generate_password_hash(payload['password']), payload['cpf'], payload['email'])
            )
        except IntegrityError as e:
            return 'ERROR IN SQL QUERY -> ' + e.args[0], 400
        except Exception as e:
            return 'Unknow error'
        else:
            db.commit()

        return 'Welcome {0}'.format(payload['fullname']), 200

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
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')

    if not request.get_json():
        return 'No json was passed', 400

    payload = request.get_json()

    if not 'cpf' in payload.keys():
        return 'No CPF was passed', 400
    if not 'password' in payload.keys():
        return 'No Password was passed', 400

    db = get_db()
    try:
        retorno = db.execute(
        'SELECT cpf, password FROM dealer where cpf = ?;', (payload['cpf'],)
        ).fetchone()
    except IntegrityError as e:
            return 'ERROR IN SQL QUERY -> ' + e.args[0], 400
    except Exception as e:
        return 'Unknow error'
    else:
        if retorno is None:
            return 'Nobody with this CPF in database', 400
        else:
            if check_password_hash(retorno['password'], payload['password']):
                token = create_access_token(identity=payload['cpf'])
                return {'Authorization': token}
            else:
                print(retorno['password'], payload['password'])
                return 'Wrong Password', 400

    return 'Something was wrong', 200



@dealer_api.route('/cashback', methods=['GET'])
@jwt_required
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
    current_app.logger.info('Info level log')
    current_app.logger.warning('Warning level log')

    current_user_cpf = get_jwt_identity()

    result = requests.get('https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323',
                            headers={'token': 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'})
    result = json.loads(result.text)
    result['cpf'] = current_user_cpf
    return result, 200