from django.db import models

class Main_win(models.Model):
    title = models.CharField(max_length=50)
    background = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_me = models.ImageField(upload_to='images/', null=True, blank=True)
    about_me = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.title




class my_skills(models.Model):
    skill = models.CharField(max_length = 50)
    progress = models.CharField(max_length = 4)

   
    def __str__(self):
        return self.skill
        

class my_services(models.Model):
    icon = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title        