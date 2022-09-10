from django.contrib import admin
from django.urls import path
from . import views
from .views import next

urlpatterns = [
    path('top/', views.top),
    # path('next/', next.as_view(), name="next"),
    path('next/', views.next, name="next")
]