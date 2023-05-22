from django.urls import include, path
from rest_framework import routers
# from django.conf.urls.static import static
# from django.conf import settings

from ecom.views import CategoryViewSet, ItemViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ItemViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
   path('', views.home)
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
