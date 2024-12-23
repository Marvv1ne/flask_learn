from flask import Flask, jsonify, request

from data import generate_companies

companies = generate_companies(100)
app = Flask(__name__)

@app.route('/')
def index():
    return 'open something like (you can change id): /companies/5'


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    return 'Hello from GET /users'


@app.route('/companies/<id>')
def get_compenies(id):
    for company in companies:
        if company['id'] == int(id):
            return company
    return 'Page not found lololo', 404