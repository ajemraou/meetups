from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='meetups_index'),
    path('<slug:meetup_slug>/success/', views.confirm_registration, name='registration_success'),
    path('<slug:meetup_slug>/', views.meetup_detail, name='meetup_detail'),
]