from django.db import models

# Create your models here.

class Course(models.Model):
    """
    Model to represent a course offered by the institution.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
