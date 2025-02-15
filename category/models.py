from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL Slug")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Parent Category")
    description = models.TextField(blank=True, null=True, verbose_name="Category Description")
    cat_image = models.ImageField(upload_to='photo/categories', blank=True, null=True, verbose_name="Category Image")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['category_name']  # Changed from 'name' to 'category_name'
        
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the category_name if not provided
        if not self.slug:
            self.slug = slugify(self.category_name)  # Changed from 'name' to 'category_name'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Generate a URL for the category detail view
        return reverse('category_detail', kwargs={'slug': self.slug})