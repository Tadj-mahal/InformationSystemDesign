from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CreatingForms.as_view(), name='submit'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)