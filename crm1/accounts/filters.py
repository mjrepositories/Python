import django_filters
from .models import *
# we are importing DateFilter and CHarfilter
from django_filters import DateFilter, CharFilter

# we are building a python class that will create a filter for us
class OrderFilter(django_filters.FilterSet):

    # we are going to create some custom atributes
    # field name is the naming of the field we will use
    start_date = DateFilter(field_name='date_created',lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    # icontains means ignoring sensitivity
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        # we need minimym two arguments
        model = Order
        # fields indicates which fields we want to allow
        fields = '__all__'

        # by creating an exclude list we are indicating what fields
        # need to be excluded from the filter
        exclude = ['customer','date_created']
