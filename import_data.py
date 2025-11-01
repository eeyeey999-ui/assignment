import os
import django
import json
from datetime import date, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from library.models import Author, Book, Review

def clean_text(text):
    return text.strip().title()

def load_data():
    with open('sample_data.json', 'r') as f:
        return json.load(f)

def import_authors(authors):
    for data in authors:
        Author.objects.update_or_create(
            email=data['email'],
            defaults={
                'name': clean_text(data['name']),
                'birth_date': datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
            }
        )

def import_books(books):
    for data in books:
        try:
            author = Author.objects.get(email=data['author_email'])
            Book.objects.update_or_create(
                title=data['title'],
                defaults={
                    'publication_date': datetime.strptime(data['publication_date'], '%Y-%m-%d').date(),
                    'author': author,
                    'genre': clean_text(data['genre'])
                }
            )
        except Author.DoesNotExist:
            print(f"Author not found: {data['author_email']}")

def import_reviews(reviews):
    for data in reviews:
        try:
            book = Book.objects.get(title=data['book_title'])
            Review.objects.update_or_create(
                reviewer_name=data['reviewer_name'],
                book=book,
                defaults={
                    'rating': int(data['rating']),
                    'comment': data['comment'].strip(),
                    'review_date': datetime.strptime(data['review_date'], '%Y-%m-%d').date()
                }
            )
        except Book.DoesNotExist:
            print(f"Book not found: {data['book_title']}")

def serialize(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    return obj

def export_data():
    authors = [
        {
            "name": author.name,
            "email": author.email,
            "birth_date": author.birth_date.isoformat()
        }
        for author in Author.objects.all()
    ]

    books = [
        {
            "title": book.title,
            "publication_date": book.publication_date.isoformat(),
            "genre": book.genre,
            "author_name": book.author.name,
            "author_email": book.author.email
        }
        for book in Book.objects.select_related('author').all()
    ]

    reviews = [
        {
            "reviewer_name": review.reviewer_name,
            "rating": review.rating,
            "comment": review.comment,
            "review_date": review.review_date.isoformat(),
            "book_title": review.book.title,
            "book_author": review.book.author.name
        }
        for review in Review.objects.select_related('book__author').all()
    ]

    with open('exported_data.json', 'w') as f:
        json.dump({'authors': authors, 'books': books, 'reviews': reviews}, f, indent=2)

def main():
    data = load_data()
    import_authors(data['authors'])
    import_books(data['books'])
    import_reviews(data['reviews'])
    export_data()
    print("Data import/export complete.")

if __name__ == '__main__':
    main()

# def export_data():
    #authors = list(Author.objects.values())
    #books = list(Book.objects.values())
    #reviews = list(Review.objects.values())
    #with open('exported_data.json', 'w') as f:
        #json.dump({'authors': authors, 'books': books, 'reviews': reviews}, f, indent=2, default=serialize)




