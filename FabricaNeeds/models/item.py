from django.db import models
from FabricaNeeds.models import Category

class Item(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="items")
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = "Items"