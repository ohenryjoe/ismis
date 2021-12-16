from django.contrib import admin
from django.urls import path, include

from hrms import urls  as hrmsurl, views as hrmsviews
from . import views

urlpatterns = [
    path('', hrmsviews.employees, name='employee'),

]