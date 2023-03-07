from django.urls import path
from .views import BookList  , BookDetail,ChapterList,ChapterDetail,ChaptersByBookBubuBubaBubuBuba,FavortiesList,FavortesByUserBubuBubaBubuBuba,BookListDetails

app_name = 'api'

urlpatterns = [
    path('books/<int:pk>/', BookDetail.as_view(), name='detailcreate'),
    path('books/', BookList.as_view(), name='listcreate'),
    path('chapters/', ChapterList.as_view(), name='listcreate'),
    path('chapters/<int:pk>/', ChapterDetail.as_view(), name='detailcreate'),
    path('books/chapters/', ChaptersByBookBubuBubaBubuBuba.as_view(), name='detailcreate'), ##http://127.0.0.1:8000/api/books/chapters/?pk=1
    path('favorites/', FavortiesList.as_view(), name='detailcreate'),
    path('Myfavorites/', FavortesByUserBubuBubaBubuBuba.as_view(), name='detailcreate'),
    path('search/', BookListDetails.as_view(), name='search'),
]