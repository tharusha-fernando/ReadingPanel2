from django.db import models
##from django.contrib.auth.models import Us
from  django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    description=models.TextField(null=True)

    cover_photo = models.ImageField(
        _("Cover_photo"), upload_to=upload_to, default='posts/default.jpg')
    date=models.DateTimeField(default=timezone.now())
    User=models.ManyToManyField(settings.AUTH_USER_MODEL)

    objects=models.Manager()
    def __str__(self):
        return self.name



class Chapter(models.Model):
    class ChpaterObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published').filter(date__lte=timezone.now())

    class ChapterFilterByBooks(models.Manager):
        ##bookId=0
        ##def __init__(self,book_id):
            ##self.bookId=book_id
        ##dffdfdd
        def get_queryset(self,book_id):
            return super().get_queryset().filter(book=book_id).order_by('-chapter_number')

    ##class ChapterByBookBubuBubaBubuBuba(models.Manager):
        ##def get_queryset(self,):


    options=(('draft','DRAFT'),('published','PUBLISHED'))
    chapter_number=models.IntegerField()
    chapter_name=models.CharField(max_length=200,null=True)
    data=models.TextField()
    date=models.DateTimeField(default=timezone.now())
    status=models.CharField(max_length=200,choices=options,default='published')
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    objects=models.Manager() #default Manager
    chapterobjects=ChpaterObjects() # only published
    chapterbook=ChapterFilterByBooks()

    class Meta:
        ordering=('id',)

    def __str__(self):
        self.chapter_number
