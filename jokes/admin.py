from common.admin import DjangoJokesAdmin
from django.contrib import admin

from .models import Category, Joke, JokeVote, Tag


@admin.register(Category)
class CategoryAdmin(DjangoJokesAdmin):
    model = Category
    list_display = ["category", "created", "updated"]

    def get_readonly_field(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")
        return ()


@admin.register(Joke)
class JokeAdmin(DjangoJokesAdmin):
    model = Joke

    # List Attributes
    date_hierarchy = "updated"
    list_display = ["question", "category", "updated"]
    list_filter = ["updated", "category", "tags"]
    ordering = ["-updated"]
    search_fields = ["question", "answer"]

    # Form Attributes
    autocomplete_fields = ["tags", "user"]
    radio_fields = {"category": admin.HORIZONTAL}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated", "vote_summary")

        return ()

    def vote_summary(self, obj):
        return f"{obj.num_votes} votes. Rating: {obj.rating}."


@admin.register(JokeVote)
class JokeVoteAdmin(DjangoJokesAdmin):
    model = JokeVote
    list_display = ["joke", "user", "vote"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("created", "updated")
        return ()


@admin.register(Tag)
class TagAdmin(DjangoJokesAdmin):
    model = Tag
    list_display = ["tag", "created", "updated"]
    search_fields = ["tag"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")
        return ()
