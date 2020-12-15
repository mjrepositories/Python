from .models import Item
import django_filters

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['thing','city','zone','category']