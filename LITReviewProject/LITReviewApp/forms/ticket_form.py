from django import forms
from ..models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "file-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title and description and title.lower() in description.lower():
            raise forms.ValidationError(
                "The description should not simply repeat the title."
            )
        
        if title and len(title) < 5:
            raise forms.ValidationError(
                "The title must contain at least 5 characters."
            )

        return cleaned_data
