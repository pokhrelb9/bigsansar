from django.db import models
from bigsansar.contrib.sites.models import domains
from django.contrib.auth.models import User

# Create your models here.

class css(models.Model):
    domain = models.OneToOneField(domains, on_delete=models.CASCADE)
    css = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain.domain

    class Meta:
        verbose_name = 'Css'
        verbose_name_plural = 'Custom Css'

    def get_absolute_url(self):
        return "http://%s/styles.css" % (self.domain,)
    

class javascript(models.Model):
     domain = models.OneToOneField(domains, on_delete=models.CASCADE)
     javascript = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
         return self.domain.domain
     
     class Meta:
         verbose_name = 'Javascripts'
         verbose_name_plural = 'JavaScripts'
         
         
     def get_absolute_url(self):
         return "http://%s/javascript.js" % (self.domain,)
     
