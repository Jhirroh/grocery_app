from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GroceryListCreateAPIView, GroceryRetrieveUpdateDeleteAPIView, ProductListCreateAPIView, \
    ProductRetrieveUpdateDeleteAPIView, MarketListCreateAPIView, MarketRetrieveUpdateDeleteAPIView

router = DefaultRouter()
router.register('groceries', GroceryViewSet, basename='grocery')
router.register('products', ProductViewSet, basename='product')
router.register('markets', MarketViewSet, basename='market')

urlpatterns = [

]

urlpatterns += router.urls
