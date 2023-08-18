from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример временной базы данных (список словарей)
books = []


# Модель "Книга"
class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year


# Маршруты для CRUD операций
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(len(books) + 1, data['title'], data['author'], data['year'])
    books.append(book)
    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/books', methods=['GET'])
def get_books():
    book_list = [{'id': book.id, 'title': book.title,
                  'author': book.author, 'year': book.year} for book in books]
    return jsonify(book_list)


@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book.id == id), None)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year})
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book.id == id), None)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    book.year = data['year']
    return jsonify({'message': 'Book updated successfully'})


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
