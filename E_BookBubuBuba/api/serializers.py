from rest_framework import serializers
##from ..app.models import Book
from django.apps import apps
from django.conf import settings
##from ..users.models import NewUser

Book=apps.get_model('app','Book')
Chapter=apps.get_model('app','Chapter')
users=apps.get_model('users','NewUser')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('id','name','author','category','description','cover_photo','date')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields=('id','chapter_number','chapter_name','data','book','date')




class FavoriteSerializer(serializers.ModelSerializer):
    User=serializers.PrimaryKeyRelatedField(queryset=users.objects.all(),many=True)

    class Meta:
        model=Book
        fields=('id','name','User')