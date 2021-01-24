"""links_dev_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from core import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # api
    path('api/', RedirectView.as_view(url='/api/v1/')),
    path('api/v1/', include('core.urls')),

    # home-page
    path('', RedirectView.as_view(url='/links/')),

    # login
    path('login/', views.login_user),
    path('login/submit', views.submit_login),

    # logout
    path('logout/', views.logout_user),

    # register-User
    path('register/', views.register_user),

    # links-page
    path('links/', views.list_links),
    path('links/new/', views.new_link),
    path('links/new/submit', views.submit_link),
    path('links/new/delete/<int:id_link>/', views.delete_link),

    # page-preview
    path('linkfree/<username>/', views.template_user),
    path('linkfree/<username>/redirect/<int:id_link>/', views.redirect_url),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
