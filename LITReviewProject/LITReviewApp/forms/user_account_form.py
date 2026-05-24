from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from ..models import UserProfile



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "display_name",
            "short_bio",
            "website",
            "profile_picture",
        ]

        widgets = {
            "display_name": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Display name (optional)",
            }),
            "short_bio": forms.Textarea(attrs={
                "class": "textarea textarea-small",
                "placeholder": "A few lines about you, your reading preferences, your favorite genres...",
                "maxlength": "500",
                "data-counter-target": "bio-counter",
            }),
            "website": forms.URLInput(attrs={
                "class": "input",
                "placeholder": "https://...",
            }),
            "profile_picture": forms.ClearableFileInput(attrs={
                "class": "file-input",
                "accept": "image/*",
                "data-preview-target": "profile-picture-preview",
            }),
        }


class StyledPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Current password",
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "Current password",
        }),
    )

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "New password",
        }),
    )

    new_password2 = forms.CharField(
        label="Confirmation",
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "Confirm new password",
        }),
    )