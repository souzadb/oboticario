from flask import Flask
from flasgger import Swagger
from api.routes.dealer import dealer_api
from api.routes.sale import sale_api

import os


def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title':   'O Boticario - Desafio Backend'
    }
    app.config.from_mapping(DATABASE=os.path.join('./database', 'boticario.sqlite'))

    swagger = Swagger(app)

    app.register_blueprint(dealer_api, url_prefix='/api/dealer')
    app.register_blueprint(sale_api, url_prefix='/api/sale')

    from database import db
    db.init_app(app)

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)