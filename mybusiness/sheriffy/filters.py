from .models import Item
import django_filters

class ItemFilter(django_filters.FilterSet):
    naming = django_filters.CharFilter('thing',lookup_expr='icontains')
    city_name = django_filters.CharFilter('city',lookup_expr='icontains')
    class Meta:
        model = Item
        fields = ['thing','city','zone','category']