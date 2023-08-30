# serializers can be used to create filtered views for your API. 
# say for a specific type of API request you want to send only the first three attributes, for such kind of purpose you'd use this serializers.py

from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price"
        ]