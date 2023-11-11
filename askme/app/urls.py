from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('user_settings/', views.user_settings, name='user_settings'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('tag/<str:tag>/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot')
    

]
