from django_filters.rest_framework import FilterSet
from .models import Space, Property, Subdivision

class SpaceFilter(FilterSet):
    class Meta:
        model = Space
        fields = {
            'city': ['exact'],
            'type': ['exact'],
            'price': ['gt', 'lt']
        }


class SubdivisionFilter(FilterSet):
    class Meta:
        model = Subdivision
        fields = {
            'city': ['exact'],
            'type': ['exact'],
            'price': ['gt', 'lt']
        }


class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'category': ['exact'],
            'city': ['exact'],
            'type': ['exact'],
            'bedrooms': ['exact'],
            'bathrooms': ['exact'],
            'rooms': ['exact'],
            'price': ['gt', 'lt']
        }