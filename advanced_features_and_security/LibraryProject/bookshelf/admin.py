from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["name", "date_of_birth"]
    search_fields = ["name"]
    list_filter = ["name"]

admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
