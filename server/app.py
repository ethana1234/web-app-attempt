from flask import Flask, jsonify, abort, request
from flask_cors import CORS

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
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
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
        try:
            books.append({
                'title': post_data['title'],
                'author': post_data['author'],
                'read': post_data['read']
            })
        except KeyError:
            abort(406, description='Invalid book input')
        existing_titles = [d['title'] for d in books]
        existing_authors = [d['author'] for d in books]
        if post_data.get('title', '') in existing_titles and post_data.get('author', '') in existing_authors:
            abort(409, description='Book already added')
        response_object['message'] = f'{post_data.get("title")} by {post_data.get("author")} added!'
    else:
        response_object['books'] = books
    return jsonify(response_object)

if __name__=='__main__':
    app.run(debug=debug)