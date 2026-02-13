from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email'}))
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'id': 'phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'id': 'message'}), required=True)