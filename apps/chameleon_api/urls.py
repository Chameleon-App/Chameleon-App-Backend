from django.urls import path
from .views import *

urlpatterns = [
    path("colors/list/", ColorListView.as_view()),
    path("colors/today/", DailyColorsView.as_view()),
    path("photos/rate/", PhotoRatingView.as_view()),
    path("photos/today/", TodayPhotoRating.as_view()),
]
