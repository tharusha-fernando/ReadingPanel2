from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Book)
class AdminUser(admin.ModelAdmin):
    list_display = ('name','id','author','category','description','date')
    ##prepopulated_fields =

admin.site.register(models.Chapter)


