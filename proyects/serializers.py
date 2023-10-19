from rest_framework import serializers
from .models import proyect
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=proyect
        fields=('id','title','description','technology','created_at')
        read_only_fields=('created_at',) #esto es para que solo puedan leer no actualizar ni eliminar

