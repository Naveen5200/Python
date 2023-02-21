from django.urls import path
from . import views
#creating list of all urls using path for url routing
urlpatterns = [
    path('', views.index,name='index'), 
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('create',views.create,name='create'),
    path('post/<str:pk>',views.post,name='post'),
    path('counter', views.counter,name='counter')
    # in views.index "views" is name of file and "index" is a function in that file.
    
]