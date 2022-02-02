from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        #self.username is provided by PermissionsMixin
        return "@{}".format(self.username)
