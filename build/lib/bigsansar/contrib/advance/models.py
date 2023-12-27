from django.db import models
from bigsansar.contrib.sites.models import domains
from django.contrib.auth.models import User

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class admin_update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField(default='bigsansar.com/dashboard',)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'update'
        verbose_name_plural = 'Admin Update'