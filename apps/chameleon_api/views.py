from rest_framework.generics import *
from .serializers import *


class ColorListView(ListAPIView):
    serializer_class = ColorSerializer
    queryset = PantoneColor.objects.all()
