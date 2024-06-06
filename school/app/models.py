from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name='Class name')


    def __str__(self):
        return self.name



class Teacher(models.Model,Class):
    fullname = models.CharField(max_length=100, verbose_name='Teacher fullname')
    age = models.IntegerField(verbose_name='Teacher age')
    price=models.IntegerField(verbose_name='Teacher price')
    class_name = models.ManyToManyField(Class, related_name='Class')


    def __str__(self):
        return self.fullname

class Student(models.Model,Class):
    fullname = models.CharField(max_length=100, verbose_name='Student fullname')
    age = models.IntegerField(verbose_name='Student age')
    class_name=models.ForeignKey(Class, verbose_name='Class name')

    def __str__(self):
        return self.fullname

