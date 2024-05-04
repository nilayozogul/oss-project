from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Martı", "author": "Richard Bach"},
    {"id": 2, "title": "Beyaz Diş", "author": "Jack London"},
    {"id": 3, "title": "Satranç", "author": "Stefan Zweig"},
    {"id": 4, "title": "Mutatio", "author": "Erhan Kolbaşı"},
    {"id": 5, "title": "Bülbülü Öldürmek", "author": "Harper Lee"}
]

# Ana sayfa
@app.route('/', methods=['GET'])
def index():
    return "Açık Kaynak Kodlu Kütüphane"

# Tüm kitapları getiren endpoint
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Belirli bir kitabı getiren endpoint
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Yeni bir kitap ekleyen endpoint
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify(new_book), 201

# Bir kitabı güncelleyen endpoint
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Bir kitabı silen endpoint
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
