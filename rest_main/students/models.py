from django.db import models

# Create your models here.
class students(models.Model):
    student_id=models.CharField(max_length=100, primary_key=True)
    branch=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name