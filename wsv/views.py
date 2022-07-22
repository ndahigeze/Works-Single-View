from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView

from wsv.models import WorkMetadata
from wsv.serializers import MetadataSerializer


class GetMetadata(RetrieveAPIView):
    queryset = WorkMetadata.objects.all()
    serializer_class = MetadataSerializer
    lookup_field = 'iswc'
