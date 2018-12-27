from django.shortcuts import render
from django.template import loader
def help(request):
    v={'insert_me':"Iam a Begginers of django"}
    return render(request,'cap/main.html',v)
