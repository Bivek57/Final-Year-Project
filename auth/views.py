from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site    #provides the current domain for the site
from django.http import HttpResponse   
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str  # convert the string to bytes and viseversa
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode # Encode and decode data in base64 format to send data in URL!!

from app.mailer import mail_system

from .verification_token import account_activation_token


def login_user(request):
    """
    views to login the user taking input from login.html form and authenticating the user
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(
                request, messages.INFO, f"{username} Logged in successfully"
            )
            return redirect("market")
        else:
            messages.add_message(request, messages.INFO, "Invalid Credentials")
            return redirect("login")
    return render(request, "auth/login.html")


def logout_user(request):
    # views to logout the user
    logout(request)
    messages.add_message(request, messages.INFO, "Logged out successfully")
    return redirect("home")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        # create a inactive user
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, "Email already exists")
        else:
            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()

            # send activation link to user
            current_site = get_current_site(request)
            mail_subject = "Activate your account | CarSansar"
            mail_template = "mailtemp/verification_mail.html"
            context = {
                "user": user,
                "domain": current_site.domain,
                "uid": (urlsafe_base64_encode(force_bytes(user.pk))),
                "token": account_activation_token.make_token(user), #making token based on user id
            }
            mail_system(
                param_mail_subject=mail_subject,
                param_template_name=mail_template,
                param_context_mail=context,
                param_user_mail=user.email,
            )
            messages.add_message(
                request,
                messages.INFO,
                "Activate your account, link sent to your mail",
            )

    return render(request, "auth/register.html")


def activate(request, uidb64, token):    #decoding token and finding the user associated with the token
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))  # force_string => convert bytes to string, urlsafe_base64_decode -> convert base64 to bytes
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token): 
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "auth/password_reset.html"  # override default template name with custom template
    email_template_name = "auth/password_reset_email.html"  # template to send email for forgot password
    subject_template_name = "auth/password_reset_subject"  # Subject for email
    success_message = "Password reset link sent to your mail"  # success message after successful apssword reset
    success_url = reverse_lazy("home")


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "auth/change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("home")
