from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Laptop(models.Model):
    description = models.TextField()
    price = models.CharField(max_length=50)
    link = models.URLField()
    company_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    ram = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)
    screen_type = models.CharField(max_length=50)
    processor_generation = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    reviews = models.TextField(blank=True, null=True)  # To be added later
    tags = models.CharField(max_length=255, blank=True, null=True)  # To be added later
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.company_name}-{self.product_name}-{self.processor_generation}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (Product: {self.product.name})"


class Review(models.Model):

    """Customer reviews for laptops."""
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name="laptop_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # 1-5 stars
    title = models.CharField(max_length=255)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.laptop.name} ({self.rating} stars)"
    




class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.URLField()
    description = models.TextField()
    category =models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)
