from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .models import UserHabit, ActivityLog, Goal
from django.http import HttpResponseForbidden

@login_required
def dashboard(request):
    user_habits = UserHabit.objects.filter(user=request.user)
    user_goals = Goal.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'user_habits': user_habits,
        'user_goals': user_goals
    })

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:  
        return HttpResponseForbidden("Nemate dozvolu za pristup ovoj stranici.")
    return render(request, 'admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html') 


class CustomLoginView(auth_views.LoginView):
    http_method_names = ['get', 'post']
    template_name = 'login.html'

class CustomLogoutView(auth_views.LogoutView):
    http_method_names = ['get', 'post']
    template_name = 'logout.html'
