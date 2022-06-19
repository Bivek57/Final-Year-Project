from django.contrib.auth import views as auth_views
from django.urls import path

from auth.views import ChangePasswordView, ResetPasswordView

from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),                                 # login user
    path("logout/", views.logout_user, name="logout"),                              # logout user
    path("signup/", views.signup, name="signup"),                                   # signup user
    path("activate/<uidb64>[0-9A-Za-z_\-]+)/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/",views.activate,name="act",), # activate user
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),    # reset password url
    path("password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html"  # change default template for password reset template html.
        ),
        name="password_reset_confirm",
    ),                                        
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("password-change/", ChangePasswordView.as_view(), name="password_change"),
]
