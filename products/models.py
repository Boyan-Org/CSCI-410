from django.db import models

# Create your models here.
class Product(models.Model): # Inherient from the default django model
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField(default="0")
    summary     = models.TextField(default="This is not cool!")


