from django.contrib import admin
from django.urls import path,include
from .views import SnackListView,SnackDetailsListView
urlpatterns = [
path('',SnackListView.as_view(), name="snacks"),
path('<int:pk>/',SnackDetailsListView.as_view(), name="snacks_detail")
]