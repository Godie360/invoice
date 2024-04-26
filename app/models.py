from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Invoice(models.Model):
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_at

