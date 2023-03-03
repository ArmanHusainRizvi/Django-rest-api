from django.db import models

# Create your models here.
#====================IN MODELS.py we have created models using class function=============
#===============and we have created four models charfields for movies crud management========
#==============then i have listed my app in stteing.py and also listed restframework=========
#==============after creating models i have run make migrations and migrate in terminal======


class movie (models.Model):
    movie_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    producer_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)
    