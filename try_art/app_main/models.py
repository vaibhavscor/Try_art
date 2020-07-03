from django.db import models

# Create your models here.
class images_log(models.Model):
    title = models.CharField(max_length=500)
    images_pic = models.FileField(null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title



    