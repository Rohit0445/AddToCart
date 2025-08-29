from django.db import models

# Create your models here.

class Item(models.Model):
    itemname = models.CharField(max_length=200)   # For storing item name
    itemPrice = models.IntegerField()  # For price with decimals
    itemImage = models.ImageField(upload_to='items/')  # Stores image in MEDIA/items/

    def __str__(self):
        return self.itemname
