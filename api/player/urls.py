from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'captain', views.CaptainHomeView)


urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.Signup),
    path('logout/', views.Logout),
    path('login/', views.Login)
]