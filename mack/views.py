from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, Consola, OrdenDeReparacion
from .serializers import ClienteSerializer, ConsolaSerializer, OrdenDeReparacionSerializer

class ClienteList(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetail(APIView):
    def get_object(self, id):
        try:
            return Cliente.objects.get(id=id)
        except Cliente.DoesNotExist:
            return None

    def get(self, request, id):
        cliente = self.get_object(id)
        if cliente is not None:
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        cliente = self.get_object(id)
        if cliente is not None:
            serializer = ClienteSerializer(cliente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        cliente = self.get_object(id)
        if cliente is not None:
            cliente.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class ConsolaList(APIView):
    def get(self, request):
        consolas = Consola.objects.all()
        serializer = ConsolaSerializer(consolas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsolaDetail(APIView):
    def get_object(self, serial):
        try:
            return Consola.objects.get(serial=serial)
        except Consola.DoesNotExist:
            return None

    def get(self, request, serial):
        consola = self.get_object(serial)
        if consola is not None:
            serializer = ConsolaSerializer(consola)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, serial):
        consola = self.get_object(serial)
        if consola is not None:
            serializer = ConsolaSerializer(consola, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, serial):
        consola = self.get_object(serial)
        if consola is not None:
            consola.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class OrdenDeReparacionList(APIView):
    def get(self, request):
        ordenes = OrdenDeReparacion.objects.all()
        serializer = OrdenDeReparacionSerializer(ordenes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdenDeReparacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdenDeReparacionDetail(APIView):
    def get_object(self, numero_orden):
        try:
            return OrdenDeReparacion.objects.get(numero_orden=numero_orden)
        except OrdenDeReparacion.DoesNotExist:
            return None

    def get(self, request, numero_orden):
        orden = self.get_object(numero_orden)
        if orden is not None:
            serializer = OrdenDeReparacionSerializer(orden)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, numero_orden):
        orden = self.get_object(numero_orden)
        if orden is not None:
            serializer = OrdenDeReparacionSerializer(orden, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numero_orden):
        orden = self.get_object(numero_orden)
        if orden is not None:
            orden.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)