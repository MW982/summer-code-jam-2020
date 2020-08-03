from django.urls import path
from main.views import HomeView, RegisterView, LoginView, LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post/<int:id>', PostView.as_view(), name='post'),
]
