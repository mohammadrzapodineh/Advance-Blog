from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# get user Model Form Project
User = get_user_model()

class Post(models.Model):
    '''
    This Class Can Defiend posts in blog app
    '''
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()


    def __str__(self):
        return self.title

    def get_absloute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Category(models.Model):
    name = models.CharField(max_length=110)
    