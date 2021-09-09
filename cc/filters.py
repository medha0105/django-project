import django_filters
from django_filters import CharFilter
from .models import *


class FoodFilter(django_filters.FilterSet):
    food = CharFilter(field_name="item", lookup_expr='icontains')