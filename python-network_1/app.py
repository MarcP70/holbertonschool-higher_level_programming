#!/usr/bin/python3
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# task 0 & 4
@app.route('/status')
def status():
    return 'OK'

# task 1
@app.route('/get_header')
def get_header():
    x_request_id = request.headers.get(
        'X-Request-Id', 'No X-Request-Id header found')
    return f'The X-Request-Id header value is: {x_request_id}'


# task 2 & 6
@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    return f'Your email is: {email}'

# task 3 & 7
@app.route('/')
def index():
    return 'Index'


# task 3 & 7
@app.route('/status_401')
def status_401():
    abort(401)


# task 3 & 7
@app.route('/status_500')
def status_500():
    abort(500)

# task 8
@app.route('/search_user', methods=['POST'])
def search_user():
    letter = request.form.get('q', '')
    if letter == 'a':
        return jsonify({'id': 8446, 'name': 'amnirqhtfjq'})
    elif letter == 'b':
        return jsonify({'id': 7094, 'name': 'bmofakakhke'})
    else:
        return jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
