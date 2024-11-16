# backend/inventory/models.py

from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
