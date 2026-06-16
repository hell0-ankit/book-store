from django.shortcuts import render, redirect

# Create your views here.
def loginViews(request):
    return render(request, 'accounts/login.html')

def signupViews(request):
    return render(request, 'accounts/signup.html')

def forgetViews(request):
    return render(request, 'accounts/forget-password.html')

def verifyOTPViews(request):
    return render(request, 'accounts/verify-otp.html')

def resend_otp(request):
    return redirect("verify_otp")

def reset_password(request):
    return render(request, 'accounts/verify-otp.html')