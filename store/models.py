from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    product_name = models.CharField( max_length=50)
    slug = models.SlugField()
    description = models.TextField( max_length=550)
    price = models.IntegerField()
    image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    stock  = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_data = models.DateTimeField( auto_now_add=True)
    modified_date = models.DateTimeField( auto_now_add=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self .product_name
    
variation_category_choice={
    ('color','color'),
    ('size','size')
}

class Variation(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category =models.CharField( max_length=50, choices=variation_category_choice) 
    variation_value=models.CharField(max_length=50)
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.product
    