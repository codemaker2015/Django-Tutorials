from django.urls import path
from . import views
urlpatterns = [
    path('q',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('hello',views.abc,name='abc')
]
