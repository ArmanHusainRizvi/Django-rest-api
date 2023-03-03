#============ then after that in views.py i have imported my model and model serializer
# to define them properly  =============
# and will self created a modelviewset class that will provide crud operations





from rest_framework.viewsets import ModelViewSet
from .models import movie
from .serializer import movieSerializer

class movieset(ModelViewSet):
    serializer_class=movieSerializer
    queryset= movie.objects.all()