"""Initialize Flask app."""
import flask_cors
import os

import server.config as configs
import server.extensions.DB as DB

DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DIR)


def apply_configuration(app, config):
    """Apply the given configuration to a flask app"""

    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('_config.py', silent=True)
    elif isinstance(config, configs.CONFIG):
        # load the config as Config object
        app.config.from_object(config)
    else:
        # load the config as mapping if passed in
        app.config.from_mapping(config)

    flask_cors.CORS(app, resources={r'*': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['TIMEOUT'] = 120
    return app


def _load_performance_requests(app):
    return app


def _init_extensions(app):
    """apply all extensions to the given app"""

    # initialise database
    DB.init_app(app)


def _init_routes(app):
    # Import parts of our core Flask app
    import server.routes


def configure_app(app, config=configs.ProductionConfig()):
    """applies all steps required to build flask app"""

    # configure root app
    app = apply_configuration(app, config)

    # initialise extensions (db)
    _init_extensions(app)

    with app.app_context():
        # initialise routes

        _init_routes(app)

    return app
