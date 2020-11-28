from flask import Flask
from flasgger import Swagger
# from api.routes.dealer import dealer_api
from api.routes.sale import sale_api

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title':   'O Boticario - Desafio Backend'
    }

    swagger = Swagger(app)

    # app.register_blueprint(dealer_api, url_prefix='/api')
    app.register_blueprint(sale_api, url_prefix='/api')

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)