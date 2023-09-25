from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from grocery.models import Market, Product, Grocery
from .serializers import MarketSerializer, ProductSerializer, GrocerySerializer


class GroceryViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                     GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer


class ProductViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MarketViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                    GenericViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

