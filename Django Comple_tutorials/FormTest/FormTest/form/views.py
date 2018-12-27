from django.shortcuts import render
from form.forms import UserForm

# Create your views here.
def index(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            #DO somthing
            print('Name: '+form.cleaned_data['name'])
            print('Age: '+form.cleaned_data['age'])
            print('text: '+form.cleaned_data['text'])
        else:
            print("Form is invalid")
    return render(request,'index.html',{'res':form})
