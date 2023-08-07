"""Application entry point"""
from server import configure_app
from flask import Flask
import server.config as configs

app = Flask(__name__, static_folder='client/build', static_url_path='')

app = configure_app(app, config=configs.TestConfig())


if __name__ == "__main__":
    app.run(debug=False, port=5000, threaded=True)
