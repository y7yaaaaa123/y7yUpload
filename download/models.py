
from django.db import models

# Create your models here.
class FilesAdmin(models.Model):
    a=models.FileField(upload_to='media_cdn',null=True)
    t=models.CharField(max_length=50)
    def __str__(self):
        return self.t
    
    def delete(self, *args, **kwargs):
        if self.a:
            self.a.delete()
        super().delete(*args, **kwargs)