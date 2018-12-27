from django.shortcuts import render
from app.models import Topic,WebPage,AccessRecord

# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpages_list}
    return render(request,'index.html',context=date_dict)
