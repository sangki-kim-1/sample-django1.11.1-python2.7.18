from django.contrib import admin
from django.urls import path

from .views import getMember, getMemberForId

urlpatterns = [
  path('', getMember),
  path('<int:id>/', getMemberForId)
]