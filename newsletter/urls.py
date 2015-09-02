from django.conf.urls import url, include
from newsletter import views

urlpatterns =[
    url(r'^$',views.index, name="index"),
]