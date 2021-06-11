from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.db.models.deletion import CASCADE
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=40)
#     price = models.FloatField(default=0, validators=[MinValueValidator(0)])
#     phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")]  ,max_length=20, null = True)
    description = models.TextField(null=True)
    image=models.ImageField(upload_to = "images", null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
#     location = models.CharField(max_length=40)
    e_date = models.DateField()
    description = models.TextField(null=True)
    event_type = models.ForeignKey(to=Service, on_delete=CASCADE, null=True, blank=True)
    image=models.ImageField(upload_to = "images", null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Vender(models.Model):
    name = models.CharField(max_length=40)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")]  ,max_length=20, null = True)
    email = models.EmailField(null=True)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    category = models.ForeignKey(to=Category, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
# product ko category ko link kiya hai show karne ke liya

class News(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    n_date = models.DateField()
    image=models.ImageField(upload_to = "images", null=True)
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.subject
