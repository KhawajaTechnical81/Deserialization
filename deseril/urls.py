from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stucreate/', views.student_create)
]
