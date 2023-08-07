"""Describes Flask configurations

All config files must inherit from the base CONFIG class. Configs must not impliment any funcitons.
Configs in an inheritance tree should avoid overlapping attribute names
"""
import os

import dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PAR_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))


class CONFIG:
    """Base CONFIG class, any object which inherits from this is considered a flask configuration object"""
    CONFIG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMP_DIR = f'{PAR_DIR}/client/public'
    pass


class SQLAlchemyConfig(CONFIG):
    """Database config Class"""

    # Set Database to the given environ varaible, else, create and operate from local db file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'production.db'))


class SQLAlchemyConfig_TESTING(CONFIG):
    """Database config Class"""
    # Set Database to the given environ varaible, else, create and operate from local db file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'testing.db')


class ProductionConfig(SQLAlchemyConfig, CONFIG):
    """Flask configuration variables."""

    # General Config
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Assets
    LESS_BIN = os.environ.get('LESS_BIN')
    ASSETS_DEBUG = os.environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = os.environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = os.environ.get('COMPRESSOR_DEBUG')
    TESTING = False


class TestConfig(SQLAlchemyConfig_TESTING, CONFIG):
    """Flask configuration variables."""

    # General Config
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Assets
    LESS_BIN = os.environ.get('LESS_BIN')
    ASSETS_DEBUG = os.environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = os.environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = os.environ.get('COMPRESSOR_DEBUG')
    TESTING = True


TEST_CONFIG = TestConfig
PRODUCTION_CONFIG = ProductionConfig
