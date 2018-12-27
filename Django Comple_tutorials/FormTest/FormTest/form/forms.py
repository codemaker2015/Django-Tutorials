from django import forms
class UserForm(forms.Form):
    name=forms.CharField(label="Enter Name")
    age=forms.CharField(label="Enter Age")
    text=forms.CharField(widget=forms.Textarea)
