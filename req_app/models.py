from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Request(models.Model):
    asunto = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_ocurrencia = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Asunto: ' + self.asunto + ' - Cliente: ' + self.cliente + ' - Estado: ' + self.getState()
    
    def getState(self):
        return 'Resuelto' if self.done else 'Pendiente'