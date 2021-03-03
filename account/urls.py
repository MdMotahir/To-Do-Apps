from django.urls import path, include

from account.views import SignUpView, UserDetailView, UserUpdateView, password_reset_complete

urlpatterns = [
    path('',include("django.contrib.auth.urls")), #this one for all login, logout, password_change etc
    path('SignUp',SignUpView.as_view(),name='SignUp'),
    path("<int:pk>",UserDetailView.as_view(),name='User Details'),

    path('<int:pk>/Update',UserUpdateView.as_view(),name='User Update'),

    path('password_reset_complete',password_reset_complete,name='password_reset_complete'),
]
