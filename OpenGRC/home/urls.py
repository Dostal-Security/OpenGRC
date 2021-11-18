from django.conf.urls import url
from home import views

urlpatterns = [
    url("", views.IndexView, name="index"),
]
