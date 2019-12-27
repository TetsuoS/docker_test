# coding=utf-8
from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSOM_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'test!'
    })


if __name__ == '__main__':
    app.run()
