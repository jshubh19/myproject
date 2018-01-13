from django.db import models

# Create your models here.



class Publisher(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    aname=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.aname

class Book(models.Model):
    title=models.CharField(max_length=10)
    author=models.ManyToManyField(Author)
    publisher=models.CharField(max_length=20)


class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(blank='true')
    salary=models.IntegerField()

    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_duration=models.IntegerField()
    fee=models.IntegerField()

    def __str__(self):
        return self.course_name

class Subject(models.Model):
    title=models.CharField(max_length=20)
    fee=models.IntegerField()
    course=models.ManyToManyField(Course)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title