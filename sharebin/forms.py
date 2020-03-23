# Django Imports
from django import forms


# Local Imports
from .models import Share


# Bootstrap class for form inputs
form_input_class = 'form-control'


class PasteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PasteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': form_input_class, 'placeholder': 'Share Name'}
        )
        self.fields['text'].widget.attrs.update(
            {'class': form_input_class, 'placeholder': 'Your text here'}
        )
        self.fields['syntax'].widget.attrs.update(
            {'class': 'custom-select'}
        )
        self.fields['expiry_duration'].widget.attrs.update(
            {'class': 'custom-select'}
        )

    class Meta:
        model = Share
        fields = ("name", "text", "syntax", "expiry_duration")
