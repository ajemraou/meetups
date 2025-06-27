from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='meetups_index'),
    path('meetups/success/', views.confirm_registration, name='registration_success'),
    path('meetups/<slug:meetup_slug>/', views.meetup_detail, name='meetup_detail'),
]