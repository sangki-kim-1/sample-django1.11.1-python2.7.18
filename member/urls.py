from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import member_details, member_create_read_all

urlpatterns = [
  url(r'^$', member_create_read_all),
  url(r'(?P<id>\d+)/$', member_details),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
