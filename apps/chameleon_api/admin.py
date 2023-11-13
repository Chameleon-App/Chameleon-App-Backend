from django.contrib import admin
from .models import PantoneColor, PantoneColorPrototype, DailyColors, RatedPhoto

admin.site.register([PantoneColor, PantoneColorPrototype, DailyColors, RatedPhoto])
