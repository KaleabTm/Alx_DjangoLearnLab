from django.contrib import admin
from .models import Author, Librarian, Library

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

class LibrarianAdmin(admin.ModelAdmin):
    model = Librarian
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

class LibraryAdmin(admin.ModelAdmin):
    model = Library
    list_display = ["name"]
    search_fields = ["name"]

admin.site.register(Author,AuthorAdmin)
admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Library,LibraryAdmin)

