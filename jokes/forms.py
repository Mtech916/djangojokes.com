from django.forms import ModelForm, Textarea

from .models import Joke


class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ["question", "answer"]
        widgets = {
            "question": Textarea(attrs={"cols": 80, "rows": 3, "autofocus": True}),
            "answer": Textarea(
                attrs={"cols": 80, "rows": 3, "placeholder": "Make it funny!"}
            ),
        }
        help_texts = {"question": "no dirty jokes please."}
