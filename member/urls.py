from django.conf.urls import url, include

from .views import get_members, get_member_for_id

urlpatterns = [
  url(r'^$', get_members),
  url(r'(?P<id>\d+)/$', get_member_for_id),
]