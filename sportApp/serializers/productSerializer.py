from rest_framework import serializers
from sportApp.models.productos import productos

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = ['nombre', 'precio', 'categoria']
