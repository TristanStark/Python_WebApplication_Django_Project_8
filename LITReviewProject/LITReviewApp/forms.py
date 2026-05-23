from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title and description and title.lower() in description.lower():
            raise forms.ValidationError(
                "La description ne doit pas simplement répéter le titre."
            )
        
        if title and len(title) < 5:
            raise forms.ValidationError(
                "Le titre doit comporter au moins 5 caractères."
            )

        return cleaned_data