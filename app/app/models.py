from django.db import models


class Singer(models.model):
    name = models.CharField()

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    district = models.CharField('Район', max_length=150)
    description = models.CharField('Описание')
    image = models.ImageField('Фото', upload_to='places/')
    singers = models.ManyToManyField(Singer)
