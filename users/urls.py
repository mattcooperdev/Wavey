from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_author/<str:username>', views.authorprofile, name='author_profile'),
    path('edit_profile/', views.editProfile, name='edit-profile'),
    path('delete_profile/', views.deleteProfile, name='delete-profile'),
]
