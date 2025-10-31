from django.contrib import admin
from .models import Author, Book, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birth_date')
    search_fields = ('name', 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'publication_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'book', 'rating', 'review_date')
    search_fields = ('reviewer_name', 'book__title')
    list_filter = ('rating', 'review_date')

#Old cmd for admin.py
#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Review)

# Register author, book and review
