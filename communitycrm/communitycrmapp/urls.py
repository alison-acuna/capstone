from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^new', views.new, name='new'),
    url(r'^display', views.display, name='display'),
    url(r'^member/(?P<id>\d+)/', views.member_item, name='member'),
    url(r'^search', views.search, name='search'),
]
