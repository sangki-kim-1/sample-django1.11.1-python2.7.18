from django.conf.urls import url, include

from .views import get_members, get_member_for_id

urlpatterns = [
  url('', get_members),
  url('<int:id>/', get_member_for_id)
]