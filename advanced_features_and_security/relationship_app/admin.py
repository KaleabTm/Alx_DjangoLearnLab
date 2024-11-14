from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Author, Librarian, Library

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["name", "date_of_birth"]
    search_fields = ["name"]
    list_filter = ["name"]

class AuthorAdmin(UserAdmin):
    model = Author
    list_display = ["name", "date_of_birth"]
    search_fields = ["name"]
    list_filter = ["name"]

class LibrarianAdmin(UserAdmin):
    model = Librarian
    list_display = ["name", "date_of_birth"]
    search_fields = ["name"]
    list_filter = ["name"]

class LibraryAdmin(admin.ModelAdmin):
    model = Library
    list_display = ["name"]
    search_fields = ["name"]

admin.site.register(User,CustomUserAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Library,LibraryAdmin)

