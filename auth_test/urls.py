"""
URL configuration for auth_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from members.views import *

urlpatterns = [
    path('landing/', landing_page, name = 'landingpage'),
    path('signup/', signup, name = 'signup'),
    path('signin/', signin, name = 'signin'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('signout/', signout, name = "signout"),
    path('profile/', profile_page, name = "profile"),
    path('quicktest/', quicktest, name = "quicktest"),
    path('specialists/', specialists, name = "specialists"),
    path('appointments/<int:id>/', appointments, name = "appointments"),
    path('Analyze/', Analyze, name = "Analyze"),
    path('Editprofile/', Editprofile, name = "Editprofile"),
    path('quicktest1/', quicktest1, name = "quicktest1"),
    path('send-email/', send_email_view, name='send_email_url'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
