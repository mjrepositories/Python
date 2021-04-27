#  As for api - we have to create serializers files so that our data will be turned into JSON or pulled from JSON
from rest_framework import serializers

from .models import Status,Period

# Imports for enabling Periods saving
import datetime
import calendar

from django.db.models import Q





# Now let's go to ModelSerializer

class StatusSerializer(serializers.ModelSerializer):
    # by declaring the slug_field in SlugRelatedField - we are able to read the title of the report instead of having it as only id indicated
    # report = serializers.SlugRelatedField(read_only=True, slug_field='title')
    # reporting_period = serializers.SlugRelatedField(read_only=True, slug_field='month')
    report = serializers.StringRelatedField(many=False)
    reporting_period = serializers.StringRelatedField(many=False)

    # Getting current year and month and enabling only periods from current month
    month_name = calendar.month_name[datetime.datetime.today().month]
    year_value = datetime.datetime.today().year
    periods = Period.objects.filter(Q(month=month_name)&Q(year=year_value))
    # executed_on =serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=periods)
    executed_on = serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=periods)
    

    # executed_on =serializers.SlugRelatedField(many=False,read_only=False,slug_field="reporting_period",queryset=Period.objects.all())


    #  In ModelSerializer we declare class Meta and there we have to put model we want to serialize and fields that we want to process
    # by doing that we will be able to transfer our data via JSON format which is readable by other technologies
    # So we used Serialization for transforming the data to something else than Python elements like dictionaries, tuples, etc.
    class Meta:
        model = Status
        fields = '__all__'