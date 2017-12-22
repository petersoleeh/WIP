from django.conf.urls import url
from . import views

urlpatterns=[
    #The landing page
    url(r'^$',views.index,name='index')
]
