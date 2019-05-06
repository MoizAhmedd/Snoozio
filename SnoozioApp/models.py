from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
import re
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    age = models.CharField(max_length = 20)
    work_time = models.CharField(max_length=20)
    exercise_time = models.CharField(max_length=20)
    calories = models.CharField(max_length=20)
    sleeptime = 0




    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('success',args=[str(self.user.id)])

def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver,User)