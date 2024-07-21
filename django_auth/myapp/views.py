from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')
        user = authenticate(request, username=username_email, password=password)
        
        if user is None:
            try:
                user = User.objects.get(email=username_email)
                user = authenticate(request, username=user.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username/email or password')
    return render(request, 'myapp/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'myapp/signup.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        
        if user:
            # token
            token = default_token_generator.make_token(user)
            # UID
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # Create password reset URL
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Send email
            send_mail(
                'Password Reset Instructions',
                f'Click the following link to reset your password: {reset_url}',
                'noreply@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset instructions have been sent to your email')
        else:
            messages.error(request, 'Email not found')
    return render(request, 'myapp/forgot_password.html')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Password changed successfully')
                return redirect('login')
            else:
                messages.error(request, 'Old password is incorrect')
        else:
            messages.error(request, 'New passwords do not match')
    return render(request, 'myapp/change_password.html')

@login_required
def dashboard_view(request):
    return render(request, 'myapp/dashboard.html')

@login_required
def profile_view(request):
    return render(request, 'myapp/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')
