from django import forms


class ContactMe(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(label="Your name please", max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=100)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
