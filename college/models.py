from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator

class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    def __str__(self):
        return "%s (%s)" % (self.name, self.hod)


class Notice(models.Model):
    subject = models.CharField(max_length = 100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add = True)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    sem = models.IntegerField(default=1, choices=((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)))
    marks_10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    marks_12 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    marks_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rn = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True, unique=True)
    pn = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
#     pip install Pillow==6.0.0 --user
#     pip install django-crispy-forms
    myimg=models.ImageField(upload_to = "images\\", null=True)
    myresume=models.FileField(upload_to = "doc\\", null=True)
    def __str__(self):
        return "%s" % self.user

class Question(models.Model):
    subject = models.CharField(max_length = 100)
    msg = models.TextField(verbose_name="Question")
    cr_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.subject
