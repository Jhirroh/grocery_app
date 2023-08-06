from django.urls import path

from .views import SignupAPIView, LoginAPIView, LogoutAPIView, ProfileRetrieveAPIView, ProfileEditAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('<str:user__username>/', ProfileRetrieveAPIView.as_view()),
    path('<str:user__username>/edit/', ProfileEditAPIView.as_view()),
]