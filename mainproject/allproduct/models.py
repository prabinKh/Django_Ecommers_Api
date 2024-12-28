from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Laptop(models.Model):
    """Model to represent a laptop product."""
    # Unique identifiers and basic details
    laptop_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)  # e.g., MacBook Pro
    brand = models.CharField(max_length=255)  # e.g., Apple, Dell, HP
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, editable=True)
    category = models.CharField(max_length=255, default="Laptops")
    currency = models.CharField(max_length=10, default="USD")

    # Specifications
    processor = models.CharField(max_length=255, blank=True, null=True)  # e.g., Intel i7
    ram = models.CharField(max_length=50, blank=True, null=True)  # e.g., 16GB
    storage = models.CharField(max_length=50, blank=True, null=True)  # e.g., 512GB SSD
    gpu = models.CharField(max_length=255, blank=True, null=True)  # e.g., NVIDIA RTX 3060
    screen_size = models.CharField(max_length=50, blank=True, null=True)  # e.g., 15.6-inch
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # in kilograms

    # Pricing and stock
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField()

    # Images
    image1 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    image2 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    image3 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)

    # Metadata
    views = models.PositiveIntegerField(default=0)
    purchases = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    tags = models.ManyToManyField('Tag', blank=True, related_name="laptops")
    reviews = models.ManyToManyField('Review', blank=True, related_name="laptops")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} {self.name}"


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
