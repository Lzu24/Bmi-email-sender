from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('services/', views.services, name = "services"),
    path('contact/', views.contact, name = "contact"),
    path('bmi/', views.bmi, name="bmi"),
    path('success/',views.success, name="success")

]