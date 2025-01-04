from django.db import models

class Apple(models.Model):
    html_filename = models.CharField(max_length=255, null=True, blank=True)
    image1 = models.URLField(max_length=500, null=True, blank=True)
    image2 = models.URLField(max_length=500, null=True, blank=True)
    image3 = models.URLField(max_length=500, null=True, blank=True)
    image4 = models.URLField(max_length=500, null=True, blank=True)
    product_title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    display_size = models.CharField(max_length=255, null=True, blank=True)
    battery_power = models.CharField(max_length=255, null=True, blank=True)
    ram = models.CharField(max_length=255, null=True, blank=True)
    internal_storage = models.CharField(max_length=255, null=True, blank=True)
    primary_camera = models.CharField(max_length=255, null=True, blank=True)
    unnamed:_18 = models.CharField(max_length=255, null=True, blank=True)
    secondary_camera = models.CharField(max_length=255, null=True, blank=True)
    chipset = models.CharField(max_length=255, null=True, blank=True)
    operating_system = models.CharField(max_length=255, null=True, blank=True)
    processor = models.CharField(max_length=255, null=True, blank=True)
    sim_type = models.CharField(max_length=255, null=True, blank=True)
    show_countdown = models.CharField(max_length=255, null=True, blank=True)
    warranty = models.CharField(max_length=255, null=True, blank=True)
    insurance = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    display_size = models.CharField(max_length=255, null=True, blank=True)
    display_type = models.CharField(max_length=255, null=True, blank=True)
    resolution = models.CharField(max_length=255, null=True, blank=True)
    cpu = models.CharField(max_length=255, null=True, blank=True)
    gpu = models.CharField(max_length=255, null=True, blank=True)
    ram = models.CharField(max_length=255, null=True, blank=True)
    storage = models.CharField(max_length=255, null=True, blank=True)
    battery = models.CharField(max_length=255, null=True, blank=True)
    operating_system = models.CharField(max_length=255, null=True, blank=True)
    features = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Apple"
        verbose_name_plural = "Apples"

    def __str__(self):
        return self.product_title if hasattr(self, "product_title") else str(self.id)
