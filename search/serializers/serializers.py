from rest_framework import serializers
from search.models import Person,Country,Region, UnknownPerson


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class UnknownPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnknownPerson
        fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    region = RegionSerializer()
    class Meta:
        model = Person
        fields = "__all__"
