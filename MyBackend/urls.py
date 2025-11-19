from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'registration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('', views.home_view, name='home_html'),
    path('login/', views.login_view, name='login_html'),
]
