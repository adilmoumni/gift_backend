"""gift_backend URL Configuration

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
from django.urls import path
from django.conf.urls import include, url  # noqa
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from gift.viewset import GiftViewSet
from category.viewset import CategoryViewSet
from product.viewset import ProductViewSet , ImageProductViewSet
from rest_framework_swagger.views import get_swagger_view
from keywords.viewset import KeywordsViewSet
from suplayer.viewset import SuplayerViewSet
from customer.viewset import CustomerViewSet
from order.viewset import OrderViewSet, OrderItemViewSet
from favored.viewset import FavoredViewSet

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='gift_backend')

router.register('gift', GiftViewSet)
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('ImageProduct', ImageProductViewSet)
router.register('keywords', KeywordsViewSet)
router.register('suplayer', SuplayerViewSet)
router.register('customer', CustomerViewSet)
router.register('order', OrderViewSet)
router.register('orderItem', OrderItemViewSet)
router.register('favored', FavoredViewSet)


urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
