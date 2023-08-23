from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.user.username}"
    
    