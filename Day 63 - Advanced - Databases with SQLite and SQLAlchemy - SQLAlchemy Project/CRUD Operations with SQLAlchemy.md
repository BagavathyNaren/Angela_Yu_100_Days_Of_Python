CRUD Operations with SQLAlchemy
Database Setup
python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Note: As of flask-sqlalchemy version 3.1+, you must pass a subclass of DeclarativeBase to the database constructor.

Creating a Table
python
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()
Note: The Mapped type annotation is used for explicit type declaration and enables SQLAlchemy to type-check data.

CRUD Operations
CREATE - Add New Record
python
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
Note: The primary key field is optional and will be auto-generated if omitted:

python
new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
READ - Retrieve Records
Read All Records:

python
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
Read Specific Record by Query:

python
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
UPDATE - Modify Records
Update by Query:

python
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()
Update by Primary Key:

python
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # Alternative: book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
DELETE - Remove Records
python
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # Alternative: book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
Key Points
Use scalars() to get individual elements from query results (multiple records)

Use scalar() to get a single element from a query result

db.get_or_404() is a convenient Flask-SQLAlchemy method for retrieving records

Previous query methods like Book.query.get() are deprecated in Flask-SQLAlchemy 3.0+

Always use db.session.commit() to persist changes to the database