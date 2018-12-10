from flask import Flask, jsonify, request
from api import app

app = Flask(__name__)

books = []

@app.route('/')
def index():
    return 'This is our book store api'

@app.route('/api/v1/books', methods = ['POST'])
def add_book():
    data = request.get_json()

    name = data.get('name')
    author = data.get('author')
    publisher = data.get('publisher')

    if not name or name.isspace():
        return jsonify({
            'message':'name is rquired'
        })
    if not author or author.isspace():
        return jsonify({
            'message':'author is rquired'
        })
    if not publisher or publisher.isspace():
        return jsonify({
            'message':'publisher is rquired'
        })

    book_id = len(books)+1

    book = dict(
        book_id = book_id,
        name = name,
        author = author,
        publisher = publisher
    )

    books.append(book)

    return jsonify({
        'message':'book added successfully',
        'book': book
    })

@app.route('/api/v1/books', methods=['GET'])
def get_all_books():
    return jsonify({
        'books':books
    })

