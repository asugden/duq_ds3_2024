import flask

app = flask.Flask('API')


@app.route('/')
def heartbeat():
    return flask.jsonify({'status': True})


@app.route('/math', methods=['GET'])
def run_math():
    number = flask.request.args.get('number')
    return flask.jsonify({'status': True, 'number': number*10})


app.run(port=8000)
