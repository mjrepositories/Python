from .models import Airlane
import django_filters

class AirFilter(django_filters.FilterSet):
    class Meta:
        model = Airlane
        fields = ['origin_country','origin_port','dest_country','dest_port','laneid']