from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CompletedTrade)
admin.site.register(models.Statistic)
admin.site.register(models.BackupStatistic)