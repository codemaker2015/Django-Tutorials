from django.shortcuts import render
from demo.forms import UserForm

def index(request):
	
	if request.method=="POST":
		form = UserForm(request.POST)
		print('Name',form.cleaned_data['name'])
	return render(request,'index.html',{'res':form})