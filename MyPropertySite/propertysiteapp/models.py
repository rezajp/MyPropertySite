from django.db import models


class Agency(models.Model):
    name=models.CharField(max_length=50)
    address_line1= models.CharField(max_length=100)
    address_line2= models.CharField(max_length=100)
    town= models.CharField(max_length=100)
    county= models.CharField(max_length=100)
    post_code= models.CharField(max_length=20)
    phone= models.CharField(max_length=100)

class Property(models.Model):
    address_line1= models.CharField(max_length=100)
    address_line2= models.CharField(max_length=100)
    town= models.CharField(max_length=100)
    county= models.CharField(max_length=100)
    post_code= models.CharField(max_length=20)
    longitude= models.DecimalField(decimal_places=10,max_digits=20)
    latitude =models.DecimalField(decimal_places=10,max_digits=20)
    type_of_property = models.ForeignKey('PropertyType', null=False)
    no_of_bedrooms=models.IntegerField()
    no_of_bathrooms=models.IntegerField()
    agency = models.ForeignKey('Agency', null=False,related_name='properties')
    
class PropertyType(models.Model):
    name=models.CharField(max_length=50)

class Advertisement(models.Model):
    for_property= models.ForeignKey('Property',null=False)
    description=models.TextField()
    slot_start=models.DateTimeField()
    slot_end=models.DateTimeField()
    created_at=models.DateTimeField()
    class Meta:
        abstract=True
class Sale(Advertisement):
    price=models.DecimalField(null=False,decimal_places=10,max_digits=20)

class Rent(Advertisement):
    rent = models.DecimalField(decimal_places=10,max_digits=20)
    deposit=models.DecimalField(decimal_places=10,max_digits=20)
    available_on=models.DateField()
        
class PropertyPhoto(models.Model):
    for_property= models.ForeignKey('Property',null=False,related_name='advertisements')
    description=models.TextField()
    #photo=models.ImageField()
    
class SiteUser(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        abstract=True
        
class NormalUser(SiteUser):
    pass

class AgencyUser(SiteUser):
    agency=models.ForeignKey('Agency',null=False,related_name='users')
class Admin(SiteUser):
    pass
    