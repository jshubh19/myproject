from django.db import models

# Create your models here.



class Publisher(models.Model):
    name=models.CharField(max_length=20,blank=True)
    city=models.CharField(max_length=20,blank=True)
    country=models.CharField(max_length=20,blank=True)
    pub=models.Manager() #it change its default manager from objects to pub ...


    def __str__(self):
        return self.name

class Meta(Publisher):
    oredering=['name']
    verbose_name='my publisher table'
    abstract='True'
    proxy='True'






class Author(models.Model):
    aname=models.CharField(max_length=20,blank=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.aname

class Book(models.Model):
    title=models.CharField(max_length=10)
    author=models.ManyToManyField(Author)
    publisher=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20,blank=True)
    email=models.EmailField(blank='true')
    salary=models.IntegerField(blank=True)

    def __str__(self):
        return self.first_name
        return self.last_name

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_duration=models.IntegerField()
    fee=models.IntegerField()

    def __str__(self):
        return self.course_name

class Subject(models.Model):
    title=models.CharField(max_length=20,blank=True)
    fee=models.IntegerField(blank=True)
    course=models.CharField(max_length=20,blank=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    name=models.CharField(max_length=20,blank=True)
    last_name=models.CharField(max_length=20,blank=True)
    location=models.CharField(max_length=20,blank=True)
    email=models.EmailField(blank=True)
    image=models.ImageField(upload_to='images',blank=True)
    file=models.FileField(upload_to='files',blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=20)
    aadhar=models.CharField(max_length=20)
    bhamashah=models.CharField(max_length=20)
    mobile=models.IntegerField()
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class  Doctor(models.Model):
    Dname=models.CharField(max_length=20,blank=True)
    Ddepartment=models.CharField(max_length=20,blank=True)
    Dhospital=models.CharField(max_length=20,blank=True)
    Demail=models.EmailField(blank=True)
    Dage=models.IntegerField(null=True)
    Dfee=models.IntegerField(null=True)
    Dprofile=models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.Dname


class Person(models.Model):
    fname=models.CharField(max_length=20,blank=True)
    lname=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.fname

class Laptop(models.Model):
    per=models.OneToOneField(Person, on_delete=models.CASCADE)
    icolor=models.CharField(max_length=10,blank=True)

    #onetoonefield lone laptop to one persone related

    def __str__(self):
        return self.per


class Construction(models.Model):
    fname=models.CharField(max_length=10,blank=True)
    lname=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.fname


class Buildings(models.Model):
    construction=models.ForeignKey(Construction,on_delete=models.CASCADE) # we use foreign key cos.. many to one field
    area=models.IntegerField(blank=True)

    def __str__(self):
        return self.construction
