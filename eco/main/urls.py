from django.urls import path
from .views import dashboard, CustomLoginView, CustomLogoutView

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]