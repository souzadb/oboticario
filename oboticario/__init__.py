from flask import Flask
from flasgger import Swagger
from oboticario.dealer import dealer_api
from oboticario.sale import sale_api
from oboticario.db import init_db
from flask_jwt_extended import JWTManager

import datetime, os, logging


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(DATABASE=os.path.join(app.instance_path, 'boticario.sqlite'))
    app.config['JWT_SECRET_KEY'] = 'joker'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    app.config['SWAGGER'] = {
        'title':   'O Boticario - Desafio Backend'
    }

    jwt = JWTManager(app)
    swagger = Swagger(app)

    app.register_blueprint(dealer_api, url_prefix='/api/dealer')
    app.register_blueprint(sale_api, url_prefix='/api/sale')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def welcome():
        return 'Welcome!', 200

    from . import db
    db.init_app(app)

    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)