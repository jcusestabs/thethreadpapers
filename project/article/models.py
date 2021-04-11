from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    author              = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    creation_date       = models.DateField(null=False, blank=False)
    last_edit_date      = models.DateField(null=False, blank=False)
    title               = models.CharField(null=False, blank=False, max_length=50)
    content             = models.TextField(null=False, blank=False, max_length=2000)
    