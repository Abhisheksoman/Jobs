from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    UserRoleView,
    JobListingViewSet,
    JobApplicationViewSet,
    LogoutView,
    CreateCompany
)

router = DefaultRouter()
router.register(r'joblistings', JobListingViewSet)
router.register(r'jobapplications', JobApplicationViewSet)

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('role/',UserRoleView.as_view(),name='user-role'),
    path('company/',CreateCompany.as_view(),name='company'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]