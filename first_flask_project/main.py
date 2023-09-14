from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import ConnectionString
from models import Book
from schemas import BookSchema

app = Flask(__name__)

# Konfiguracija SQLAlchemy veze sa bazom podataka
engine = create_engine(ConnectionString)

# Kreiranje sesije za interakciju sa bazom podataka
Session = sessionmaker(bind=engine)
session = Session()


# Dohvatanje svih knjiga
@app.route('/books', methods=['GET'])
def get_all_books():
    books = session.query(Book).all()
    book_schema = BookSchema(many=True)
    result = book_schema.dump(books)
    return jsonify(result)


# Dohvatanje knjige po ID-u
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book_schema = BookSchema()
        result = book_schema.dump(book)
        return jsonify(result)
    return jsonify({'error': 'Book not found'}), 404


# Dohvatanje nove knjige
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book_schema = BookSchema()
    errors = book_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400

    new_book = Book(**data)
    session.add(new_book)
    session.commit()

    result = book_schema.dump(new_book)
    return jsonify({'message': 'Book added successfully', 'data': result}), 201


# Uređivanje knjige po ID-u
@app.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.get_json()
    book_schema = BookSchema()
    errors = book_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400

    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        for key, value in data.items():
            setattr(book, key, value)
        session.commit()
        return jsonify({'message': 'Book updated successfully'})

    return jsonify({'error': 'Book not found'}), 404


# Brisanje knjige po ID-u
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        return jsonify({'message': 'Book deleted successfully'})

    return jsonify({'error': 'Book not found'}), 404

# Filtriranje knjiga prema autoru
@app.route('/books/filter', methods=['GET'])
def filter_books_by_autor():
    autor_filter = request.args.get('autor')

    if not autor_filter:
        return jsonify({'error': 'autor is required'}), 400

    # Koristite Marshmallow shemu za serijalizaciju rezultata upita
    books = session.query(Book).filter(Book.autor.ilike(autor_filter)).all()
    book_list = BookSchema(many=True).dump(books)

    return jsonify(book_list)


if __name__ == '__main__':
    app.run()
