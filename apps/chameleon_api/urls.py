from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path("colors/list/", ColorListView.as_view()),
    path("colors/today/", DailyColorsView.as_view()),
    path("photos/rate/", PhotoRatingView.as_view()),
    path("photos/today/", TodayPhotoRating.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
