from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path("colors/list/", ColorListView.as_view()),
]
