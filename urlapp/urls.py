from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_form_view, name='url_form'),

]
