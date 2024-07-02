from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')


    # Define related_name for groups and user_permissions to resolve clashes
    # Define related_name for groups and user_permissions to resolve clashes
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.name