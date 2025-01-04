from django.db import models

class Microphone(models.Model):
    title = models.CharField(max_length=255)
    price_first = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_second = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_link = models.URLField(max_length=500, null=True, blank=True)
    product_link = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Microphone"
        verbose_name_plural = "Microphones"

    def __str__(self):
        return self.product_title if hasattr(self, "product_title") else str(self.id)
