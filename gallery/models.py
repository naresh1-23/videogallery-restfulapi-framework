
import uuid
from django.db import models
from django.core.validators import FileExtensionValidator

class BaseModel(models.Model):
    uuid  = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4())
    uploaded_at = models.DateField(auto_now= True)

    class Meta:
        abstract = True

class Gallery(BaseModel):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos', validators=[FileExtensionValidator(['mp4', 'mpv'])])
# Create your models here.
