import pytest, ast

def test_new_dealer_complete(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)
    assert response.data == b'Welcome Gijo'

def test_new_dealer_name_error(client):

    data = {
        'password': 'gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)
    assert response.data == b'No name was passed'

def test_new_dealer_password_error(client):

    data = {
        'fullname': 'Gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)
    assert response.data == b'No password was passed'

def test_new_dealer_email_error(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)
    assert response.data == b'No email was passed'

def test_new_dealer_cpf_error(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'email': 'gijo@gmail.com'
    }

    response = client.post('/api/dealer/new', json=data)
    assert response.data == b'No cpf was passed'

def test_valid_dealer(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)

    data = {
        'password': 'gijo',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/valid', json=data)
    response = response.data.decode('UTF-8')
    response = ast.literal_eval(response)
    assert 'Authorization' in response.keys()

def test_valid_dealer_error_no_cpf(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)

    data = {
        'password': 'gijo'
    }

    response = client.post('/api/dealer/valid', json=data)
    assert response.data == b'No CPF was passed'


def test_valid_dealer_error_no_password(client):

    data = {
        'fullname': 'Gijo',
        'password': 'gijo',
        'email': 'gijo@gmail.com',
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/new', json=data)

    data = {
        'cpf': '12312312323'
    }

    response = client.post('/api/dealer/valid', json=data)
    assert response.data == b'No Password was passed'