from django import forms
from .models import EmailMessage

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ['subject', 'message', 'sender_email', 'recipient_email']
