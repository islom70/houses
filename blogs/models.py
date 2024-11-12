from django.conf import settings
from django.db import models


class House(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    area = models.FloatField(help_text="Area in square meters")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(upload_to='house_images/', null=True, blank=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.buyer} - {self.house}"