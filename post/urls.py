from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]