from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image',default='profile_image/no_profile.png', blank=True, null=True)
    phone = models.CharField(max_length=13)
    Date_of_birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
