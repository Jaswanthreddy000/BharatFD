"""
URL configuration for faq_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings  # Import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq import views

from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'faqs', views.FAQViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API routes
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor URLs
    path('', views.faq_list, name='faq-list'),  # FAQ list page
    path('add/', views.add_faq, name='add-faq'),  # Add FAQ page
    # path('', RedirectView.as_view(url='/api/')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
