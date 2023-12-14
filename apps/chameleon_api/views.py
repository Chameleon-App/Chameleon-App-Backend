from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ColorSerializer, DailyColorsSerializer, RatedPhotoSerializer, UserSerializer
from .service.color_service import ColorService
from .service.photo_rater_service import PhotoRaterService
from .service.photo_service import PhotoService


class ColorListView(ListAPIView):
    serializer_class = ColorSerializer
    queryset = ColorService.get_all_colors()


class DailyColorsView(APIView):
    def get(self, request):
        snippet = ColorService.get_last_daily_color()
        serializer_class = DailyColorsSerializer(snippet)
        return Response(serializer_class.data)


class TestGenerateColorsView(APIView):
    def get(self, request):
        service = ColorService()
        service.generate_new_daily_color()
        snippet = ColorService.get_last_daily_color()
        serializer_class = DailyColorsSerializer(snippet)
        return Response(serializer_class.data)


class PhotoRatingView(APIView):
    def post(self, request):
        photo_bytes = request.FILES.get("photo").read()
        photo_rater_service = PhotoRaterService()
        rated_photo = photo_rater_service.get_rated_photo(photo_bytes)
        serializer = RatedPhotoSerializer(rated_photo)
        return Response(serializer.data)


class TopPhotosListView(ListAPIView):
    serializer_class = RatedPhotoSerializer

    def get_queryset(self):
        date = self.request.query_params.get("date", None)
        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        offset = int(self.request.query_params.get("offset", 0))
        limit = int(self.request.query_params.get("limit", 15))

        return PhotoService.get_most_rated_photos(date=date, offset=offset, limit=limit)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
