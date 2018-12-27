from . import views
from django.conf.urls import url,include

urlpattern = [
	url(r'^',views.index)
]