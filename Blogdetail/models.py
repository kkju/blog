from django.db import models
from django.db import models
from MyBlog import settings

#fs = FileSystemStorage(location='/media/photo')
# Create your models here.
class Blogs(models.Model):
    page = models.IntegerField(blank=True, help_text="Unit:MS")
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photo", blank=True)
    text = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.name