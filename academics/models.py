from django.db import models

#Creating Course Table
class Course(models.Model) :
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20 , unique=True)
    duration_years = models.PositiveBigIntegerField(default=4)

    def __str__(self):
        return self.name

    
#Creating Subject Table
class Subject(models.Model) :
    #Linknig course as Foreign Key
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10, unique=True)
    semester = models.PositiveSmallIntegerField()
    credit_hours = models.PositiveSmallIntegerField(default=3)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta : 
        ordering = ["semester" , "code"]
