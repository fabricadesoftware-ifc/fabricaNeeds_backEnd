from django.db import models

class RecurrencyType(models.Model):
    description = models.CharField(max_length=50)

    def __self__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = "RecurrencyTypes"