
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField 
from bigsansar.contrib.sites.models import domains


# Create your models here.

class post(models.Model):
    domain = models.ForeignKey(domains, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='| Bigsansar')
    slug = models.SlugField(unique=True)
    body = RichTextUploadingField()
    visitor = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "http://%s/blog/preview/%s" % (self.domain, self.id)

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
