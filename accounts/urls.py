from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^login-admin/', views.LoginAdminView.as_view()),
    url(r'^login-facebook/', views.LoginFacebook.as_view()),
    url(r'^signup-facebook/', views.SignUpFacebook.as_view()),
    url(r'^profile/', views.ProfileView.as_view()),
]
