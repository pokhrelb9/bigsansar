
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField 
from bigsansar.contrib.sites.models import domains
import time
from django.utils.text import slugify


def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / username/<y>/ <m> / <d> / <filename> >
    years = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    get_time = years + '/' + month + '/' + day

    return str("%s/%s/%s" % (instance.user.username, get_time, filename))
  
# Create your models here.

class post(models.Model):
    domain = models.ForeignKey(domains, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='| Bigsansar')
    slug = models.SlugField(unique=True)
    thumbnails = models.ImageField(upload_to=user_directory_path, blank=True)
    body = RichTextUploadingField()
    publish_date = models.DateField(auto_now_add=True)
    visitor = models.IntegerField(default=0)

    def delete(self, using=None, keep_parents=False):
        try:

            self.thumbnails.storage.delete(self.thumbnails.name)
        except:
            pass
        
        super().delete()

    def __str__(self):
        return self.title
    
    

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    # def get_absolute_url(self):
    #     return reverse("blog", kwargs={"slug": self.slug})


class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(post, on_delete=models.CASCADE)
    comments = models.TextField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
