from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menu/$', views.ProductMenuView.as_view()),
]