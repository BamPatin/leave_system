from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.html import format_html

# Create your models here.

LEAVE_CHOICE = (
    ('S','Sick Leave'),
    ('P','Personal Leave'),
    ('V','Vacation Leave'),
)

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100) #,primary_key=True)
    date = models.DateTimeField(auto_now = False, auto_now_add = True, null = False, blank = True)  
    # user = models.OneToOneField(ชื่อตารางพนักงาน,on_delete=models.CASCADE,primary_key=True,)
    typeleave = models.CharField(max_length=5 , null=True , blank=True , choices=LEAVE_CHOICE)
    numberleave = models.IntegerField()
    From_Date = models.DateField()    
    To_Date = models.DateField()    
    
    def __str__(self):
        return self.name

class Number(models.Model):
    # user = models.ForeignKey(Form,on_delete=models.CASCADE,primary_key=True)
    # name = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='name_from')
    form = models.OneToOneField(
        Form,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # user = models.CharField(max_length=100)
    sick = models.IntegerField(default=30)      #ลาป่วย
    personal = models.IntegerField(default=10)  #ลากิจ
    vacation = models.IntegerField(default=8)   #ลาพักร้อน
 
    def __str__(self):
        return self.user   
    