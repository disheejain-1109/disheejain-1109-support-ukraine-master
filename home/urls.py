from django.urls import path, include
from . import views
# from allauth.account.urls

urlpatterns = [
    # home k corresponding name soshome and will call bview sosview
    path('', views.SosView.as_view(), name='soshome'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('rescued', views.PeopleRescuedView.as_view(), name='rescued'),
    path('accounts/', include('allauth.urls')),
    path('lost-and-found/', include('lost_and_found.urls')),
    path('logout', views.LogOut, name='logout'),
    # path('login', views.LogIn, name='login')
]