from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ismingiz...*", 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': "Pochta...", 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': "Mavzu...*", 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': "Xabaringiz...", 'class': 'form-control', 'rows': 4}),
        }
