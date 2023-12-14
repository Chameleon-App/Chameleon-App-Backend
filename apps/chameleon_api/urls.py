from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *

urlpatterns = [
    path("colors/list/", ColorListView.as_view()),
    path("colors/today/", DailyColorsView.as_view()),
    path("colors/generate/", TestGenerateColorsView.as_view()),
    path("photos/rate/", PhotoRatingView.as_view()),
    path("photos/top/", TopPhotosListView.as_view()),
    path("auth/signup/", CreateUserView.as_view()),
    path("auth/token/", ObtainAuthToken.as_view()),
    path("profiles/<str:username>/", ProfileInfoView.as_view()),
    path("days/", DaysListView.as_view()),
]
