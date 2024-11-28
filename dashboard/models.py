from django.db import models

# Create your models here.
class DashboardData(models.Model):
    title = models.CharField(max_length=200)
    value = models.FloatField()
    category = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        ordering = ['-timestamp']
