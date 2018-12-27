from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'baba/index.html')
def form_name_view(request):
    form1=forms.FormName()
    dict={'form':form1}
    if request.method=='POST':
        form1=forms.FormName(request.POST)

        if form1.is_valid():
            #DO Somthing
            print("Validation is Success")
            print("NAME: "+form1.cleaned_data['name'])
            print("Email: "+form1.cleaned_data['email'])
            print("Text: "+form1.cleaned_data['text'])
    return render(request,"baba/form_page.html",dict)
