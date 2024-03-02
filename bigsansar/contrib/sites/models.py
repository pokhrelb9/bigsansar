import os
import shutil

from django.contrib.auth.models import User
from django.db import models

from www.settings import BASE_DIR


# Create your models here.


class domains(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=15, default=None)
    publish_date = models.DateField(auto_now_add=True)
    visitor = models.IntegerField(default=1)
    primary_domaIn = models.BooleanField(default=False)
    

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Custom Domain'

    def get_absolute_url(self):
        return "http://%s" % (self.domain,)

    def delete(self, using=None, keep_parents=False):
        filename = 'templates' + '/' + str(self.domain)
        try:
            full_url = os.path.join(BASE_DIR, filename)
            shutil.rmtree(full_url)

        except:
            pass

        super().delete()


class pages(models.Model):
    domain = models.ForeignKey(domains, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    visitor = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pages'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.domain.domain

    def get_absolute_url(self):
        if self.slug == 'styles':
            return "http://%s/%s.css" % (self.domain, self.slug)
        elif self.slug == 'sitemap':
            return "http://%s/%s.xml" % (self.domain, self.slug)
        elif self.slug == 'script':
            return "http://%s/%s.js" % (self.domain, self.slug)
        else:
            return "http://%s/%s" % (self.domain, self.slug)

    def delete(self, using=None, keep_parents=False):
        filename = 'templates' + '/' + str(self.domain.domain) + '/' + self.slug + '.html'
        full_url = os.path.join(BASE_DIR, filename)
        if os.path.exists(full_url):
            os.remove(full_url)
        else:
            pass

        super().delete()



class default_domain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain = models.OneToOneField(domains, on_delete=models.CASCADE)
   
    
    