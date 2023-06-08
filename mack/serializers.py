from rest_framework import serializers
from .models import Cliente, Consola, OrdenDeReparacion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'telefono', 'direccion', 'ciudad')

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = ('serial', 'marca', 'modelo', 'falla', 'accesorios', 'observaciones')

class OrdenDeReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDeReparacion
        fields = ('numero_orden', 'cliente', 'consola', 'fecha_ingreso', 'fecha_salida', 'reparacion_realizada',
                  'valor', 'tiempo_garantia', 'reparada')