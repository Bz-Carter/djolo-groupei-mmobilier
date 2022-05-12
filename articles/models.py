from djoloGroup import settings
from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'


class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """verbose_name = 'category'"""
        verbose_name_plural = 'types'


class Property(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    address = models.TextField(max_length=200)
    city = models.TextField(max_length=50)
    latitude = models.TextField(max_length=200)
    longitude = models.TextField(max_length=200)
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rooms = models.IntegerField()
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='properties', on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    photos = models.ManyToManyField('Photo', blank=True)
    videos = models.ManyToManyField('Video', blank=True)

    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    description = models.TextField(max_length=400, blank=True, default='')
    created = models.DateTimeField(auto_now=True)


class Space(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    address = models.TextField(max_length=200)
    city = models.TextField(max_length=50)
    latitude = models.TextField(max_length=200)
    longitude = models.TextField(max_length=200)
    area = models.IntegerField()
    description = models.TextField(blank=True, default='')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='spaces', on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    photos = models.ManyToManyField('Photo', blank=True)
    videos = models.ManyToManyField('Video', blank=True)

    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']


class Subdivision(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    address = models.TextField(max_length=200)
    latitude = models.TextField(blank=True, default='')
    longitude = models.TextField(blank=True, default='')
    city = models.TextField(max_length=50)
    area = models.IntegerField()
    description = models.TextField(blank=True, default='')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subdivisions', on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    photos = models.ManyToManyField('Photo', blank=True)
    videos = models.ManyToManyField('Video', blank=True)

    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']


class Photo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    alt = models.TextField(max_length=200, blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class Video(models.Model):
    name = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='videos', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class Partner(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    alt = models.TextField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']