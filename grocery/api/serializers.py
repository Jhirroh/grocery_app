from rest_framework import serializers

from grocery.models import Market, Product, Grocery


class MarketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, write_only=False)

    class Meta:
        model = Market
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, write_only=False)
    market = MarketSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'market']

    def create(self, validated_data):
        market_data = validated_data.pop('market')
        market, isMarketCreated = Market.objects.get_or_create(**market_data)
        product, isProductCreated = Product.objects.get_or_create(market_id=market.id, **validated_data)
        return product

    def update(self, instance, validated_data):
        market_data = validated_data.pop('market')
        market_id = market_data.get('id')
        market, _ = Market.objects.update_or_create(id=market_id, defaults={'name': market_data['name']})
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.market = market
        instance.save()
        return instance


class GrocerySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Grocery
        fields = ['id', 'name', 'products']

    def create(self, validated_data):
        product_datas = validated_data.pop('products', [])
        grocery = Grocery.objects.create(**validated_data)

        for product_data in product_datas:
            market_data = product_data.pop('market')
            market, isMarketCreated = Market.objects.get_or_create(**market_data)
            product, isProductCreated = Product.objects.get_or_create(market_id=market.id, **product_data)
            grocery.products.add(product)

        return grocery

    def update(self, instance, validated_data):
        product_datas = validated_data.pop('products')
        instance.name = validated_data.get('name', instance.name)
        instance.products.clear()

        for product_data in product_datas:
            market_data = product_data.pop('market')
            market_id = market_data.get('id')
            product_id = product_data.get('id')
            market, _ = Market.objects.update_or_create(id=market_id, defaults={'name': market_data['name']})
            product, _ = Product.objects.update_or_create(id=product_id,
                                                          defaults={'name': product_data['name'],
                                                                    'price': product_data['price'],
                                                                    'market': market})
            instance.products.add(product)

        instance.save()
        return instance
