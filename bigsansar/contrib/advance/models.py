from django.db import models
from bigsansar.contrib.sites.models import domains
from django.contrib.auth.models import User

# Create your models here.

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
         return "http://%s/script.js" % (self.domain,)
     
