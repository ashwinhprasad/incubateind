from django.urls import path, include
from .views import UserSignup, UserSignin, UserSignout, UserProfile

urlpatterns = [
    path('signup/',UserSignup,name='signup'),
    path('signin/',UserSignin,name='signin'),
    path('signout/',UserSignout,name='signout'),
    path('profile/',UserProfile,name='userprofile')
]
