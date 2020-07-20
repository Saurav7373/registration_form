
from django.urls import path
from . import views
urlpatterns = [
    path('',views.register, name='register'),
    path('signup/',views.signup, name='signup'),
    path('login1/',views.login1, name='login1'),
    path('logout1/',views.logout1, name='logout1'),

]
