from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rental_price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField()
    transmission_choices = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
        ('tiptronic', 'Tiptronic'),
    ]
    transmission = models.CharField(max_length=20, choices=transmission_choices)
    added_by = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    photo1 = models.ImageField(upload_to='cars/photos', blank=True, null=True)
    photo2 = models.ImageField(upload_to='cars/photos', blank=True, null=True)
    photo3 = models.ImageField(upload_to='cars/photos', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.release_year}"

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Rental of {self.car} by {self.user}"