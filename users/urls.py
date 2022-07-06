from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('borrar/<slug:slug>', views.borrar_usuario, name = 'borrar'),
    path('edit/<slug:slug>', views.edituser_list, name = 'edit'),
    path('edit2/<slug:slug>', views.edituser_view, name = 'edit2'),
    path('profile/<slug:slug>', views.user_detail, name='user_detail'),
    path('signup/', views.signup_view, name='signup'),   
    path('logout/', views.logout_view, name='logout'),
    path('change/',views.changepassword, name='change'),
    path('list/', views.user_list, name = 'list'),
    path('crear/', views.signup_view, name = 'crear'),

]