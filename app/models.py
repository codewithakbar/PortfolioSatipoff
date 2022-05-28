from re import L
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    """
    Portfolio Uchun Categoriya
    """

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    objects = models.Manager()

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("app:product_list_by_category", args=[self.slug])


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # category = models.ForeignKey(Category, related_name='app_posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    views = models.IntegerField(default=0)
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.slug])



    
class PostPortfolio(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, related_name='port_posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    urltoproject = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='portfolio/proects/%Y/%m/%d', blank=True)    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.slug])