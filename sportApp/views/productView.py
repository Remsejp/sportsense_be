# se importan para poder generar las respuestas http
from rest_framework.response import Response
# se importa para poder consumir las vistas de ayuda 
from rest_framework.views import APIView
# se importa para poder modificar las vistas de ayuda
from rest_framework.decorators import api_view
#se importa para poder usar el modelo creado
from sportApp.models import productos
# se importa para poder manipular el modelo con el serializador creado
from sportApp.serializers import productSerializer


@api_view(['GET','POST'])
def product_api_view(request):

    if request.method == 'GET':
        product = productos.objects.all()
        product_serializer = productSerializer(product, many=True)

        return Response(product_serializer.data)

    elif request.method == 'POST':
        product_serializer = productSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)

        return Response(product_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])

def product_detail_view(request,pk = None):
    
    if request.method == 'GET':
        product = productos.objects.filter(id=pk).first()
        product_serializer = productSerializer(product)

        return Response(product_serializer.data)
    
    elif request.method == 'PUT':
        product = productos.objects.filter(id=pk).first()
        product_serializer = productSerializer(instance = product, data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)

        return Response(product_serializer.errors)

    elif request.method == 'DELETE':
        product = productos.objects.filter(id=pk).first()
        product.delete()

        return Response("Eliminado")
