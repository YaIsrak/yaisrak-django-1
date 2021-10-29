from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('pictures/', views.pictures),
    # path('admin/', admin.site.url)
]