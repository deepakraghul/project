from django.db import models
from django.utils import timezone


class college(models.Model):
    student_name=models.CharField(max_length=100)
    course_taken=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    date_of_joining=models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.student_name
