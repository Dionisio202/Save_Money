from django.db import models

class proyect(models.Model):
    title =models.CharField(max_length=200) 
    description=models.TextField()
    technology =models.CharField(max_length=200)
    created_at=models.TimeField(auto_now_add=True)