from flask import Flask
from flasgger import Swagger
from api.routes.dealer import dealer_api
from api.routes.sale import sale_api

import datetime, os, logging


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

    @app.before_first_request
    def before_first_request():
        log_level = logging.INFO
    
        for handler in app.logger.handlers:
            app.logger.removeHandler(handler)
    
        root = os.path.dirname(os.path.abspath(__file__))
        logdir = os.path.join(root, 'logs')
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        log_file = os.path.join(logdir, 'app.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)
    
        app.logger.setLevel(log_level)

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)