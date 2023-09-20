from django.contrib import admin

from .models import Category, Joke


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["category", "created", "updated"]

    def get_readonly_field(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")
        return ()


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ["question", "created", "updated"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")

        return ()
