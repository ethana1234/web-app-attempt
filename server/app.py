from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import uuid

# App instantiation
app = Flask(__name__)
app.config.from_object(__name__)

# Configuration
debug = True

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Sample data
books = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# Basic route
@app.route('/ping', methods=['GET'])
def helloWorld():
    return 'Flask says: Hello World!'

# Get the books
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        existing_titles = [d['title'] for d in books]
        existing_authors = [d['author'] for d in books]
        if post_data.get('title', '') in existing_titles and post_data.get('author', '') in existing_authors:
            abort(409, description='Book already added')
        try:
            books.append({
                'id': uuid.uuid4().hex,
                'title': post_data['title'],
                'author': post_data['author'],
                'read': post_data['read']
            })
        except KeyError:
            abort(406, description='Invalid book input')
        response_object['message'] = f'{post_data.get("title")} by {post_data.get("author")} added!'
    else:
        response_object['books'] = books
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        books[:] = [book for book in books if book.get('id') == post_data.get('id', '')]
        if post_data.get('id') is None:
            post_data['id'] = uuid.uuid4().hex
        try:
            books.append({
                'id': post_data['id'],
                'title': post_data['title'],
                'author': post_data['author'],
                'read': post_data['read']
            })
        except KeyError:
            abort(406, description='Invalid book input')
        response_object['message'] = f'{post_data.get("title")} by {post_data.get("author")} updated!'
    return jsonify(response_object)

if __name__=='__main__':
    app.run(debug=debug)
