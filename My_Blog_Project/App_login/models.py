from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # one to one relation is similler to Foreign key
    # with index=unique
    user        = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return str(self.user)
