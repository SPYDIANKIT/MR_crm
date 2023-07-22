from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('success')
            else:
                form.add_error(None, 'Invalid login credentials or user is inactive.')

    else:
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})



@login_required
def success_view(request):
    return render(request, 'dashboard.html')
def dashboard_view(request):
    return render(request, 'dashboard.html')