from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    position = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username  

class Employee_Time(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    emp_h_at_work = models.BigIntegerField(null=True)
    holiday_h = models.BigIntegerField(null=True)
    sick_h = models.BigIntegerField(null=True)

    def __str__(self):
        return "%s" % (self.username)

class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Plot(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name  

class Admitting(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username)

class Team_members(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username)

class Category_of_work(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name  

class Subdivision(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name  

class Work_manager(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username) 

class Manufacturer_work_manager(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username) 

class To_observer(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username)  

class Entrusted(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username) 

class An_object(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name  

class Work_supervisor(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "%s" % (self.username)  



class create_e_naryad_table_1(models.Model):
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    plot = models.ForeignKey(Plot, null=True, on_delete=models.SET_NULL)
    admitting = models.ForeignKey(Admitting, null=True, on_delete=models.SET_NULL)
    team_members = models.ManyToManyField(Team_members)
    category_of_work = models.ForeignKey(Category_of_work, null=True, on_delete=models.SET_NULL)
    employee_preparedness_time = models.DateField()
    start_work = models.DateField()
    finish_work = models.DateField()
    subdivision = models.ForeignKey(Subdivision, null=True, on_delete=models.SET_NULL)
    work_manager = models.ForeignKey(Work_manager, null=True, on_delete=models.SET_NULL)
    manufacturer_work_manager = models.ForeignKey(Manufacturer_work_manager, null=True, on_delete=models.SET_NULL)
    to_observer = models.ForeignKey(To_observer, null=True, on_delete=models.SET_NULL)
    entrusted = models.ForeignKey(Entrusted, null=True, on_delete=models.SET_NULL)
    an_object = models.ForeignKey(An_object, null=True, on_delete=models.SET_NULL)
    workplace_preparation_text1 = models.TextField()
    workplace_preparation_text2 = models.TextField()
    workplace_preparation_text3 = models.TextField()
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

class Order(models.Model):
    number_naryad = models.IntegerField()
    technical_activities = models.CharField(max_length=200, null=True)
    place_name_work = models.CharField(max_length=200, null=True)
    work_supervisor = models.ForeignKey(Work_supervisor, null=True, on_delete=models.SET_NULL)
    team_members = models.ManyToManyField(Team_members)
    person_give_naryad =  models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    started_work = models.DateField()
    work_done = models.DateField()

    def __str__(self):
        return self.number_naryad


    


  



    



