# import flask_migrate
import flask_sqlalchemy
import sqlalchemy.exc

db = flask_sqlalchemy.SQLAlchemy(session_options={"autoflush": True})


def init_app(app):
    """Initialises the flask_SQLAlchemy database and migation for the given app"""

    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except sqlalchemy.exc.OperationalError:
            """The table has already been created by something else"""
            pass

    # migrate = flask_migrate.Migrate(app, models.db)

    return db
