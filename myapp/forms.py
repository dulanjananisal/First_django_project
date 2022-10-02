from django import forms

class FormsView(forms.Form):
    image = forms.FileField()
    text = forms.CharField()

