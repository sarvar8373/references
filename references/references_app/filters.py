import django_filters
from .models import *

class SoatoFilter(django_filters.FilterSet):
    class Meta:
        model = Soato
        fields = '__all__'
        