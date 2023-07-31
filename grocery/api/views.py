from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from grocery.models import Market, Product, Grocery
from .serializers import MarketSerializer, ProductSerializer, GrocerySerializer


class GroceryListAPIView(ListCreateAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer


class GroceryRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MarketListCreateAPIView(ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

