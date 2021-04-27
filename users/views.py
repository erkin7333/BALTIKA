from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from baltika.decorators import anonymous_required
from .models import Profile
from django.contrib.auth.decorators import login_required
from main.models import Post
from django.contrib import messages

@anonymous_required('main:index')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = request.POST['username'], password=request.POST['password1'])
            profile = Profile(image='defaulti.jpg', user_id=user.id)
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} You have been successfully authenticated now you can Log in!')
            return redirect('login')
    form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@anonymous_required('main:index')
def login_check(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('main:index')
    form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required
def logout_check(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out Thank you for visiting!')
    return redirect('main:index')

@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user.id).order_by('-post_added')
    if request.method == 'POST':
        form_u = ProfileForm(request.POST, instance=request.user)
        form_p = ProfilePicForm(request.POST, request.FILES, instance=request.user.profile)
        if form_u.is_valid() and form_p.is_valid():
            form_u.save()
            form_p.save()
            return redirect('profile')
    form_u = ProfileForm(instance=request.user)
    form_p = ProfilePicForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'form_u':form_u, 'form_p':form_p, 'posts':posts})


