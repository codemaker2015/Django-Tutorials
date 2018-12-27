from django.shortcuts import render
from app1.models import Employee
from django.http import HttpResponse
# Create your views here.
def index(request):
    data={'insert_me':"Iam index.html file "}
    return render(request,'myapp/index.html',data)
def hello(request):
    data=Employee.objects.order_by('name')
    values={'access_record':data}
    return render(request,'myapp/test.html',values)
def abc(request):
    return render(request,'myapp/hello.html')
