from django.shortcuts import redirect, render
from .forms import CustomCreationForm
from .models import Profile
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        profile = Profile()
        if form.is_valid():
            user = form.save()
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)