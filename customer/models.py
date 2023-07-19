from django.db import models

# Create your models here
class Customer(models.Model):
    from django.db import models

    class Customer(models.Model):
        id_number = models.CharField(max_length=11)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        phone = models.CharField(max_length=20)
        city = models.CharField(max_length=100)
        town = models.CharField(max_length=100)
