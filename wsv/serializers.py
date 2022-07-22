from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from wsv.models import WorkMetadata, Contributor


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class MetadataSerializer(ModelSerializer):
    contributors = serializers.SerializerMethodField()

    class Meta:
        model = WorkMetadata
        fields = "__all__"

    def get_contributors(self,obj:WorkMetadata):
        return  ContributorSerializer(Contributor.objects.filter(metadata_id=obj.id),many=True).data
