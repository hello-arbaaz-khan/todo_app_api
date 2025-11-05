from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView,SignupView, TaskViewSet
router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('', include(router.urls))
]
