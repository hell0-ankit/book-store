from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model,login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from .models import PasswordReset

User = get_user_model()

def signupViews(request):
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        # check password 
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")
        # Create User
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
        )
        messages.success(request, "Account created successfully.")
        return redirect("login")
    return render(request, 'accounts/signup.html')

def loginViews(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'accounts/login.html')

def logoutView(request):
    logout(request)
    return redirect('home')


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        if user:
            reset = PasswordReset.objects.create(user=user)
            link = (f"http://127.0.0.1:8000/accounts/reset-password/{reset.token}/")
            send_mail("Reset Password",link,"ankitbohra660@gmail.com",[email])
            messages.success( request,"Password reset link email par send kar diya gaya hai.")
        else:
            messages.error(request,"Email not found.")
    return render( request,"accounts/forgot_password.html")

def reset_password(request, token):
    reset = get_object_or_404( PasswordReset,token=token)
    user = reset.user
    if request.method=="POST":
        password = request.POST.get("password")
        confirm = request.POST.get( "confirm_password")
        if password == confirm:
            user.password = make_password(password)
            user.save()
            reset.delete()
            return redirect("login")
        else:
            messages.error(request,"Password not match")
    return render(request,"accounts/reset_password.html")



def verifyOTPViews(request):
    return render(request, 'accounts/verify-otp.html')

def resend_otp(request):
    return redirect("verify_otp")

