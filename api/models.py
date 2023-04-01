from django.db import models

class Company(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    website     = models.CharField(max_length=255, default='https://google.com')
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name        = models.CharField(max_length=100)
    color       = models.CharField(max_length=20)
    price       = models.FloatField()
    description = models.TextField(default='', blank=True)

    # relationships
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.company.name}'
    

class Category(models.Model):
    name     = models.CharField(max_length=100)
    products = models.ManyToManyField(to=Product)

    def __str__(self):
        return self.name
