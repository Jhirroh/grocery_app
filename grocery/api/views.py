from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from grocery.models import Market, Product, Grocery
from .serializers import MarketSerializer, ProductSerializer, GrocerySerializer


class GroceryListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

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

