import django
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

        
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=30, default="") 
    desc = models.CharField(max_length=300, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    userId = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    timestamp = models.DateTimeField(default=timezone.now)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.update_desc


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=15, default="")


    def __str__(self):
        return f'{self.user.username} Profile'

    # # Override the save method of the model
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image
        
    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image


