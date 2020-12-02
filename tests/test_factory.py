from oboticario import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_welcome(client):
    response = client.get('/')
    assert response.data == b'Welcome!'