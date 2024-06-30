
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language1 = models.DecimalField(max_digits=5, decimal_places=2)
    language2 = models.DecimalField(max_digits=5, decimal_places=2)
    acting = models.DecimalField(max_digits=5, decimal_places=2)
    dance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Subject marks for {self.student.name}"

