from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ColorSerializer,
    DailyColorsSerializer,
    RatedPhotoSerializer,
    UserSerializer,
    ProfileSerializer,
    DaySerializer,
)
from .service.color_service import ColorService
from .service.photo_rater_service import PhotoRaterService
from .service.photo_service import PhotoService
from .service.profile_service import ProfileService


class ColorListView(ListAPIView):
    serializer_class = ColorSerializer
    service = ColorService()
    queryset = service.get_all_colors()


class DailyColorsView(APIView):
    service = ColorService()

    def get(self, request):
        snippet = self.service.get_last_daily_color()
        serializer_class = DailyColorsSerializer(snippet)
        return Response(serializer_class.data)


class PhotoRatingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    service = PhotoRaterService()

    def post(self, request):
        photo_bytes = request.FILES.get("photo").read()
        user = request.user

        rated_photo = self.service.get_rated_photo(photo_bytes, user)
        serializer = RatedPhotoSerializer(rated_photo, context={"request": request})
        return Response(serializer.data)


class TopPhotosListView(ListAPIView):
    serializer_class = RatedPhotoSerializer
    service = PhotoService()

    def get_queryset(self):
        date = self.request.query_params.get("date", None)
        if date:
            date = datetime.strptime(date, "%Y-%m-%d").date()
        offset = int(self.request.query_params.get("offset", 0))
        limit = int(self.request.query_params.get("limit", 15))

        return self.service.get_most_rated_photos(date=date, offset=offset, limit=limit)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer


class ProfileInfoView(APIView):
    service = ProfileService()

    def get(self, request, *args, **kwargs):
        snippet = self.service.get_profile_info(self.kwargs["username"])
        serializer_class = ProfileSerializer(snippet, context={"request": request})
        return Response(serializer_class.data)


class MyProfileInfoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    service = ProfileService()

    def get(self, request, *args, **kwargs):
        snippet = self.service.get_profile_info_by_user(self.request.user)
        serializer_class = ProfileSerializer(snippet, context={"request": request})
        return Response(serializer_class.data)


class DaysListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DaySerializer
    service = ColorService()

    def get_queryset(self):
        queryset = self.service.get_all_daily_colors()
        return queryset
