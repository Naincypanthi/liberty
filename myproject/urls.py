"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add apath('', views.home, name='home')
Class-based n import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('home/<category>',views.home2),
    path('shop/<category>',views.shop),
    path('addToCart',views.addToCart),
    path('displayCart',views.displayCart),
    path('clearCart',views.clearCart),
    path('delete',views.delete),
    path('page/<id>',views.page),
    
    path('registration',views.registration),
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('invalid',views.invalid),
    path('logout',views.logout),
    path('order',views.order),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)