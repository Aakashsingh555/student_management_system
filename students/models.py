from django.db import models
from academics.models import Course


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="students",
    )

    def __str__(self):
        return self.name