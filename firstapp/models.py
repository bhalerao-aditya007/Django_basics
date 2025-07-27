from django.db import models

# Create your models here.
class Form (models.Model):
    first_name = models.CharField(max_length= 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField(("email"), max_length=254, unique=True)
    phone_number = models.CharField(max_length = 15, blank = True)
    photo = models.ImageField(upload_to='images')
    Skills = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.first_name
    
