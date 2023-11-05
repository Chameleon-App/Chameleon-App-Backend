from django.contrib import admin
from .models import PantoneColor, PantoneColorPrototype, DailyColors

admin.site.register([PantoneColor, PantoneColorPrototype, DailyColors])
