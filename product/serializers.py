from rest_framework import serializers
from .models import Users,Product,OrderDetails

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
    
class OrderDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails
        fields='__all__'