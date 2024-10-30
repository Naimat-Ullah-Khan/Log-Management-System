from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)


class Log(models.Model):
    LOG_TYPES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    log_type = models.CharField(max_length=10, choices=LOG_TYPES)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
