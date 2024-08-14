from django.urls import path
from .views import UserCreateView, LoginView, LogoutView, UserListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view,name='logout'),
    path('list/', UserListView.as_view(),  name ='user-list')
 
]