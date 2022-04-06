from django.contrib import admin
from BOOKS.models import Book

# Register your models here.
@admin.register(Book)
class Books(admin.ModelAdmin):
    list_display = ['id','title']