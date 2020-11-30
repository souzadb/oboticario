from http import HTTPStatus
from flask import Blueprint, json, request, current_app
from flasgger import swag_from
from database.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlite3 import IntegrityError
from datetime import datetime

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

    current_user_cpf = get_jwt_identity()

    if not request.args:
        return 'No data was passed', 400

    payload = request.args

    if not 'cod' in payload.keys():
        return 'No cod was passed', 400
    if not 'value' in payload.keys():
        return 'No value was passed', 400

    date = datetime.today().strftime('%Y-%m-%d')

    if current_user_cpf == '15350946056':
        status = 'APROVADO'
    else:
        status = 'EM VALIDACAO'

    db = get_db()
    try:
        db.execute(
        '''INSERT INTO sale (cod, value, date, cpf, status)
            VALUES (?, ?, ?, ?, ?)''', (payload['cod'], payload['value'], date, current_user_cpf, status)
        )
    except IntegrityError as e:
            return 'ERROR IN SQL QUERY -> ' + e.args[0], 400
    except Exception as e:
        return 'Unknow error'
    else:
        db.commit()
        return 'SUCCESS', 200

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

    current_user_cpf = get_jwt_identity()

    current_month = datetime.now().month
    print(current_month)

    db = get_db()
    try:
        result = db.execute(
        '''SELECT cod, value, date, status FROM sale WHERE cpf = ?
        AND substr(date, 6, 2) = ?''', (current_user_cpf, str(current_month))
        ).fetchall()
    except IntegrityError as e:
        return 'ERROR IN SQL QUERY -> ' + e.args[0], 400
    except Exception as e:
        return 'Unknow error -> ' + e.args[0], 400
    else:
        data = {
            'payload': {
                'sales': [],
                'CPF': current_user_cpf,
            }
        }

        result = [list(x) for x in result]

        data['payload']['sales'] = [{
                                        'cod':x[0],
                                        'value': x[1],
                                        'date': x[2],
                                        'status': x[3]
                                    }
                                    for x in result]

        total_value = sum(sale['value'] for sale in data['payload']['sales'])
        
        if total_value <= 1000:
            percent_cashback = 0.1
        elif 1000 > total_value <= 1500:
            percent_cashback = 0.15
        else:
            percent_cashback = 0.2

        for idx, _ in enumerate(data['payload']['sales']):
            data['payload']['sales'][idx]['cashback'] = data['payload']['sales'][idx]['value'] * percent_cashback
            data['payload']['sales'][idx]['cashback_percent'] = str(percent_cashback * 100) + '%'

        print(data)
        return data, 200