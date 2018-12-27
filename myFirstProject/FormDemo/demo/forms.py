from django import forms

class UserForm(forms.Form):
	name = forms.CharField(max_length=20)
	age = forms.IntegerField()
	address = forms.CharField(widget=forms.Textarea)