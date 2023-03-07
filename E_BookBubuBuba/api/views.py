##from django.shortcuts import render
import os

from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import filters
##from ..app.models import Book
from .serializers import BookSerializer,ChapterSerializer,FavoriteSerializer
from django.apps import apps
from rest_framework.permissions import SAFE_METHODS,IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

Book=apps.get_model('app','Book')
Chapter=apps.get_model('app','Chapter')


class ReadOnlyUnlessStaff(BasePermission):
    """
    Custom permission to make a view read-only unless the user is staff.
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.method in SAFE_METHODS


class BookList(generics.ListCreateAPIView, ReadOnlyUnlessStaff):
    permission_classes = [IsAuthenticated, ReadOnlyUnlessStaff]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'author']

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
        if file_obj:
            # Do something with the file
            name = request.data.get('name', 'default_name')
            file_name, file_extension = os.path.splitext(file_obj.name)
            custom_name = f"{name}{file_extension}"
            file_obj.name = custom_name
            pass


        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BookListDetails(generics.ListAPIView,ReadOnlyUnlessStaff):
    ##class PostListDetailfilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ReadOnlyUnlessStaff]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,ReadOnlyUnlessStaff]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ##pass

class ChapterList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,ReadOnlyUnlessStaff]
    queryset = Chapter.objects.all()
    serializer_class =ChapterSerializer
    pass

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,ReadOnlyUnlessStaff]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    pass

class ChaptersByBookBubuBubaBubuBuba(generics.ListAPIView):
    permission_classes = [IsAuthenticated,ReadOnlyUnlessStaff]
    serializer_class = ChapterSerializer

    def get_queryset(self):
        queryset = Chapter.chapterobjects.all()
        filter_param = self.request.query_params.get('pk')
        if filter_param:
            queryset = queryset.filter(book=filter_param).order_by('chapter_number')
        return queryset


class FavortiesList(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Book.objects.all()


class FavortesByUserBubuBubaBubuBuba(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        filter_param = self.request.query_params.get('user_id')
        if filter_param:
            queryset = queryset.filter(User=filter_param)
        return queryset



