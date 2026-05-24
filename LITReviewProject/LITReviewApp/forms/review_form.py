from django import forms

from ..models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "body", "rating"]
        widgets = {
            "headline": forms.TextInput(
                attrs={
                    "class": "input",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "textarea",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "class": "input",
                    "min": 0,
                    "max": 5,
                }
            ),
        }

