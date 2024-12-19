from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .models import UserHabit, ActivityLog, Goal
from django.http import HttpResponseForbidden
from .models import Habit
from .forms import HabitForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Goal
from .forms import GoalForm

@login_required
def dashboard(request):
    user_habits = UserHabit.objects.filter(user=request.user) 
    user_goals = Goal.objects.filter(user=request.user) 

    return render(request, 'dashboard.html', {
        'user_habits': user_habits,
        'user_goals': user_goals,
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

class HabitListView(ListView):
    model = Habit
    template_name = 'habit_list.html'
    context_object_name = 'habits'
    paginate_by = 10  
    def get_queryset(self):
        queryset = Habit.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)  

        order = self.request.GET.get('order', '')
        if order == 'points_asc':
            queryset = queryset.order_by('points')  
        elif order == 'points_desc':
            queryset = queryset.order_by('-points') 

        return queryset

class HabitDetailView(LoginRequiredMixin, DetailView):
    model = Habit
    template_name = 'habit_detail.html'

class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habit_form.html'
    success_url = reverse_lazy('habit_list')

class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habit_form.html'
    success_url = reverse_lazy('habit_list')

class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'habit_confirm_delete.html'
    success_url = reverse_lazy('habit_list')

class GoalCreateView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goal_form.html'
    success_url = reverse_lazy('dashboard')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AchievedGoalsListView(ListView):
    model = Goal
    template_name = 'achieved_goals.html'
    context_object_name = 'achieved_goals'

    def get_queryset(self):
        # Filter goals that are marked as achieved and belong to the logged-in user
        return Goal.objects.filter(user=self.request.user, achieved=True)