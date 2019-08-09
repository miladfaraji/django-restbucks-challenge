from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.OrderListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.OrderView.as_view(), name='view'),
    url(r'^(?P<pk>\d+)/cancel/$', views.CancelOrderView.as_view(), name='cancel'),

]