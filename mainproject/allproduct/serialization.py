from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields ="__all__"


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


