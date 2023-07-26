from . import views
from django.urls import path

app_name = 'bank_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form_page, name='form_page'),
    path('submit', views.submit_form, name='submit_form'),
    ]
