import flask
import gensim
import numpy as np


app = flask.Flask('API')
fasttext_model_path = 'data/cc.en.50.bin'
model = gensim.models.fasttext.load_facebook_vectors(fasttext_model_path)


@app.route('/')
def heartbeat():
    return flask.jsonify({'alive': True})

@app.route('/math', methods=['GET'])
def compute_math():
    number = float(flask.request.args.get('number'))
    return flask.jsonify({'status': True, 'number': number*10})

@app.route('/thesaurus', methods=['GET'])
def etim():
    return flask.render_template('etim.html')

@app.route('/sentence', methods=['GET'])
def sentence():
    sentence = flask.request.args.get('sentence')
    if (sentence and len(sentence) > 0):
        sentence = [v.lower() for v in sentence.split('_')]
        vecs = [model.get_vector(v) for v in sentence]
        vec = np.mean(vecs, axis=0)
        similar = model.similar_by_vector(vec, restrict_vocab=30_000)
        # Returns [('banana', 0.9), ('potato', 0.3)]
        return flask.jsonify({'success': True, 'similar': similar})


if __name__ == '__main__':
    app.run(port=8000)









# app = flask.Flask('API')


# @app.route('/')
# def heartbeat():
#     return flask.jsonify({'status': True})


# @app.route('/math', methods=['GET'])
# def run_math():
#     number = flask.request.args.get('number')
#     return flask.jsonify({'status': True, 'number': number*10})


# app.run(port=8000)


