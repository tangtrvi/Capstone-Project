from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.TextField(max_length=255)
    no_of_guest = models.SmallIntegerField(default=0)
    booking_date = models.DateTimeField(default=None)

class menu(models.Model):
    title = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    