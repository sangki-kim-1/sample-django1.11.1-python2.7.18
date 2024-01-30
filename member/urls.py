from django.conf.urls import url, include

from .views import member_details, member_create_read_all

urlpatterns = [
  url(r'^$', member_create_read_all),
  url(r'(?P<id>\d+)/$', member_details),
]