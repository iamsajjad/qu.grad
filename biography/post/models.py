from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
class Post(models.Model):

    #Post
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=256, default='', blank=False)
    url         = models.URLField(max_length=512, db_index=True, unique=True, blank=True, null=True)
    image       = models.ImageField(upload_to='posts/', blank=True, null=True)
    text        = models.TextField(default='', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.id} : {self.title}'
