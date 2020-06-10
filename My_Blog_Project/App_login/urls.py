from django.urls import path
from . import views
app_name = "App_login"
urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('user_change/',views.user_change,name='user_change'),
    path('password/',views.pass_change,name='pass_change'),
    path('add_profile_pic/',views.add_pro_pic,name='add_pro_pic'),
    path('change_profile_pic/',views.change_pro_pic,name='change_pro_pic'),

]
