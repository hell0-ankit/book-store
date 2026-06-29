from django.contrib import admin

from .models import (Category, Author,Publisher,Book,BookImages)

@admin.register(Category)
class BooksCategory(admin.ModelAdmin):
    exclude =("slug",)

@admin.register(Author)
class BooksAuthor(admin.ModelAdmin):
    exclude =("slug",)

@admin.register(Publisher)
class BooksPublisher(admin.ModelAdmin):
    fields = ("name", "publication_date")

@admin.register(Book)
class Books(admin.ModelAdmin):
    fields = ("title", "authors","publisher","categories","price","cover_image","isbn","page_count","language","description","is_active")
    

@admin.register(BookImages)
class Books_gallery(admin.ModelAdmin):
    fields = ("book","image","alt_text")
   
   
