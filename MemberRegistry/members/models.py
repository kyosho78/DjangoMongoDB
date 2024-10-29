from django.db import models
import datetime

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    membership_start_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
