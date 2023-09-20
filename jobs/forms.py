from datetime import datetime
from django import forms


class JobApplicationForm(forms.Form):
    EMPLOYMENT_TYPES = (
        (None, "--Please choose--"),
        ("ft", "Full-time"),
        ("pt", "Part-time"),
        ("contract", "Contract work"),
    )
    DAYS = (
        (1, "MON"),
        (2, "TUE"),
        (3, "WED"),
        (4, "THU"),
        (5, "Fri"),
    )
    YEARS = range(datetime.now().year, datetime.now().year + 2)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": "https://www.example.com",
                "size": "50",
            }
        )
    )
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(years=YEARS),
        help_text="The earliest date you can start working.",
    )
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        widget=forms.CheckboxSelectMultiple(attrs={"checked": True}),
        help_text="Select all days that you can work.",
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(attrs={"min": "10.00", "max": "100.00", "step": ".25"})
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={"cols": "75", "rows": "5"})
    )
    confirmation = forms.BooleanField(
        label="I cerify that the information I have provided is true."
    )
