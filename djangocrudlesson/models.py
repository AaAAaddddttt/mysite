from django.db import models

# Create your models here.
class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True,blank=False)# BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False)# VAR CHAR(55) NOT NULL
    date_created = models.DateTimeField(auto_now_add=True) #TIME S TAP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True) #TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False) #BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    fist_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    middle_name = models.CharField(max_length=55, blank=True)#varchar(55) DEFAULT NULL
    last_name = models.CharField(max_length=55, blank=False)#VARCHAR(55)NOT NULL
    age = models.IntegerField(blank=False)# INT NOT NULL
    birth_date = models.DateField(blank=False)# Date not null
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55, blank=False)
    password = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True) #TIMES TAP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True) #TIME STA MP DEFAULT CURRENT_TIME STAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'users'