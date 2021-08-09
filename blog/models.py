from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title