from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

class Consola(models.Model):
    serial = models.CharField(primary_key=True, max_length=50)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    falla = models.CharField(max_length=200)
    accesorios = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=200)
    

class OrdenDeReparacion(models.Model):
    numero_orden = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_salida = models.DateField(blank=True, null=True)
    reparacion_realizada = models.CharField(max_length=200)
    valor = models.IntegerField()
    tiempo_garantia = models.PositiveIntegerField(default=0)
    reparada = models.BooleanField(default=False)
     
    def __str__(self):
        return f"Registro #{self.id} - {self.consola.serial}"

   
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    # Otros campos adicionales para el modelo de Usuario
    
    # Campos requeridos para la implementación del modelo AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

