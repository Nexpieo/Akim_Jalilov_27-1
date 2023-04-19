from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
