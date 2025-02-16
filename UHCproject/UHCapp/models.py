from django.db import models

# Create your models here.

class FormResponse(models.Model):
    user_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.EmailField(max_length=50)
    c_myself = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Tracks submission time

    def __str__(self):
        return f"{self.user_name} - {self.subject}"