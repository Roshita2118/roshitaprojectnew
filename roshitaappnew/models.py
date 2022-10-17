# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
def __str__(self):
        return self.title