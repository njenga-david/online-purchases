from django.db import models

# Create your models here.

class Customer(models.Model):
    Name=models.CharField(max_length=200, null=True)
    Phone=models.CharField(max_length=200, null=True)
    Email=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name


    
class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)


    def __str__(self) :
        return self.name

    

class Products(models.Model):

    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Otdoor'),
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField( null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True,  blank=True)  
    date_created= models.DateTimeField(auto_now_add=True, null=True) 
    tags=models.ManyToManyField(Tag)

    def __str__(self) :
        return self.name

    






class Order(models.Model):
    STATUS=(('pending','pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered','Delivered'),
            )
    name=models.CharField(max_length=200, null=True)
    Customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    products=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True) 
    status=models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self) :
        return self.name

   
             
