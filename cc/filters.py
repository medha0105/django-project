import django_filters
from .models import *
from django_filters import DateFilter

# class FoodFilter(django_filters.FilterSet):
#     date = DateFilter(field_name="date_created")