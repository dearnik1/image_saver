from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        next_page='/url_form/'
    ), name='login'),
    path('url_form/', include('urlapp.urls')),
]
