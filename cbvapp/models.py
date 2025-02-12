from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    CEO=models.CharField(max_length=100)
    date_of_origin=models.IntegerField()
    origin=models.CharField(max_length=100)
    logo=models.ImageField(upload_to ='logos/',blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})
    
class Products(models.Model):
    product_name=models.CharField(max_length=110)
    fuel_type=models.CharField(max_length=110)
    milliage=models.IntegerField()
    tank_capacity=models.PositiveIntegerField()
    top_speed=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    color=models.CharField(max_length=50)
    CC=models.PositiveIntegerField()
    pro_image=models.ImageField(upload_to ='prod_images/',blank=True,null=True)
    company=models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

