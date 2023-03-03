#============= i have created serializer.py file to serialize my models=======
#============ i have used class again to serialize all ============

from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import movie

class movieSerializer(ModelSerializer):
    class Meta :
        model=movie
        fields = '__all__'