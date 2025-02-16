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




class FormResponse1(models.Model):
    empanelled = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    referred = models.CharField(max_length=100)
    YES_NO_CHOICES = [('YES', 'YES'),('NO', 'NO')]

    selection = models.CharField(max_length=200, choices=YES_NO_CHOICES)  # Stores either "yes" or "no"
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically records the submission time

    def __str__(self):
        return f"{self.user_name} - {self.subject}"
