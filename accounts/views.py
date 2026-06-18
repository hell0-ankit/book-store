from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def loginViews(request):
    return render(request, 'accounts/login.html')

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








def forgetViews(request):
    return render(request, 'accounts/forget-password.html')

def verifyOTPViews(request):
    return render(request, 'accounts/verify-otp.html')

def resend_otp(request):
    return redirect("verify_otp")

def reset_password(request):
    return render(request, 'accounts/reset-password.html')