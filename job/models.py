from django.db import models

"""To use the user table we've to import User from django.contrib.auth.models"""
from django.contrib.auth.models import User


# Create your models here.


class Company(models.Model):
    """Model for declaring company name"""
    comp_name = models.CharField(max_length=50)
    domain = models.CharField(max_length=10)

    objects = models.Manager()

    def __str__(self):
        return self.comp_name


class Designation(models.Model):
    """To declare the employees designation"""
    role = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return self.role


class Register(models.Model):
    """To register the employee with the following details"""

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    emp_name = models.CharField(max_length=20)
    emp_email = models.EmailField(unique=True)
    designation = models.ForeignKey(Designation, related_name="emp_role", on_delete=models.CASCADE)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default=None)
    profile_pic = models.ImageField("media/")
    comp_details = models.ForeignKey(Company, related_name="comp_info", on_delete=models.CASCADE)
    phone = models.IntegerField()
    qualification = models.CharField(max_length=20)
    experience = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.emp_name


class Employee(models.Model):
    """It'll give the all details of the Particular employee"""
    emp_details = models.OneToOneField(Register, on_delete=models.CASCADE)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    address = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return str(self.emp_details)


class Team(models.Model):
    """To store all the teams in the project"""
    team_name = models.CharField(max_length=25)
    team_members = models.ForeignKey(Employee, related_name="members", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.team_name


class MailBox(models.Model):
    """To send mails from one employee to another employee in that organisation"""
    sender = models.ForeignKey(Employee, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Employee, related_name="receiver", on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    files = models.FileField("media/")

    objects = models.Manager()

    def __str__(self):
        return str(self.sender)


class Project(models.Model):
    """ALl employees and teams for particular project"""
    project_name = models.CharField(max_length=100)
    teams = models.ForeignKey(Team, related_name="teams", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.project_name
