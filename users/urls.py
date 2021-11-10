from django.urls import path
from . import views


app_name = "users"


urlpatterns = [
	
	path('', views.AccountView.as_view(), name="account"),
	path('profile', views.profile_view, name="profile"),
	path('signup', views.SignUpView.as_view(), name="signup"),
	path('signin', views.SignInView.as_view(), name="signin"),
	path('sign-out', views.sign_out, name="sign-out"),
]