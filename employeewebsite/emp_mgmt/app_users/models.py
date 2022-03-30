from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #get filename
    if instance.user.username:
        filename ='User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture",  blank=True)
    user1 = 'user1'
    user2 = 'user2'
    user_types = [
		(user1, 'user1'),
		(user2, 'user2'),
	]
    user_type = models.CharField(max_length=10, choices=user_types, default=user1)

    def __str__(self):
        return self.user.username
