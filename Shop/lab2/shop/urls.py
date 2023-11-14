from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductList.as_view(), name='create_product'),
    path('clients/', views.ClientList.as_view(), name='clients'),
    path('orders/', views.Orderget.as_view(), name='orders'),
    # path('orders/', views.formOrderClient, name='searchclient'),
    # path('orders/', views.formOrderProduct, name='searchproduct'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
