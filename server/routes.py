"""Routes for parent Flask app."""

import json
import flask
from flask import current_app as app
from flask import send_from_directory


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/example', methods=['GET'])
def example():
    if flask.request.method == 'POST':
        # Handle POST requests if necessary
        pass
    elif flask.request.method == 'GET':

        folder_selected = flask.request.args.get('folderSelected')
        if app.config['TESTING']:
            pass

        else:
            pass

        # Return the response as a JSON object containing the progress stage
        return app.response_class(
            response=json.dumps(
                {
                    'data': None,
                }
            ),
            status=200,
            mimetype='application/json'
        )

    # Return a 'bad request' response if the method is neither POST nor GET
    return 'bad request', 400


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')



