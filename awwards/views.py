from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import Project
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ProjectPostForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    try:
        projects = Project.objects.all()
    except Exception as e:
        raise  Http404()
    return render(request, 'home.html', {'projects':projects})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def post_project(request):
    current_user = request.user
    if request.method=='POST':
        form = ProjectPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect("home")
    else:
        form = ProjectPostForm()
    return render(request,'project_post.html',{'form':form})