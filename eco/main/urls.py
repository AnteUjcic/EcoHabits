from django.urls import path
from .views import dashboard, CustomLoginView, CustomLogoutView, HabitListView, HabitDetailView, HabitCreateView, HabitUpdateView, HabitDeleteView, GoalCreateView, AchievedGoalsListView

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('habits/', HabitListView.as_view(), name='habit_list'),  # List view
    path('habit/<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),  # Detail view
    path('habit/add/', HabitCreateView.as_view(), name='habit_add'),  # Add new habit
    path('habit/<int:pk>/update/', HabitUpdateView.as_view(), name='habit_update'),  # Update habit
    path('habit/<int:pk>/delete/', HabitDeleteView.as_view(), name='habit_delete'),  # Delete habit
    path('goal/add/', GoalCreateView.as_view(), name='goal_add'),  # Add this line
    path('goals/achieved/', AchievedGoalsListView.as_view(), name='achieved_goals'),  # Add this line

]