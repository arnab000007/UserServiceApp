from django.urls import path

from UserService.views.CreateUserAPIView import CreateUserAPIView
from  UserService.views.LoginUserAPIView import LogInUserAPIView
from UserService.views.GetUserNameAPIView import GetUserNamePostAPIView, GetUserNameAPIView

urlpatterns = [
    path('signup/', CreateUserAPIView.as_view(), name='signup'),
    path('login/', LogInUserAPIView.as_view(), name='login'),
    path('getuserpost/', GetUserNamePostAPIView.as_view(), name='getuserpost'),
    path('getuser/', GetUserNameAPIView.as_view(), name='getuser'),

]