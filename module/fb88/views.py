from rest_framework import generics
from rest_framework.response import Response

from module.fb88.models import Fb88
from module.fb88.serializers import Fb88ListSerializers

class Fb88ListView(generics.ListCreateAPIView):
    serializer_class = Fb88ListSerializers

    def get_queryset(self):
        return Fb88.objects \
            .prefetch_related('questions') \
            .prefetch_related('questions__answer').filter()


# Create your views here.
