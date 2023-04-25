from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from bigsansar.contrib.sites.models import domains


# Create your models here.

class post(models.Model):
    domain = models.ForeignKey(domains, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='| Bigsansar')
    thumbnails = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    slug = models.SlugField(unique=True)
    body = RichTextField()
    visitor = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.thumbnails.storage.delete(self.thumbnails.name)
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
