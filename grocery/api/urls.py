from django.urls import path

from .views import GroceryListCreateAPIView, GroceryRetrieveUpdateDeleteAPIView, ProductListCreateAPIView, \
    ProductRetrieveUpdateDeleteAPIView, MarketListCreateAPIView, MarketRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('groceries/', GroceryListCreateAPIView.as_view()),
    path('groceries/<int:pk>/', GroceryRetrieveUpdateDeleteAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteAPIView.as_view()),
    path('markets/', MarketListCreateAPIView.as_view()),
    path('markets/<int:pk>/', MarketRetrieveUpdateDeleteAPIView.as_view()),

]
