from django.db import models
# Create your models here.
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import(
    AbstractBaseUser,BaseUserManager,PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self, username,email,password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User should have a Email')
        user = self.model(username=username , email=self.normalize_email(email),)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,email,password=None):
        if password is None:
            raise TypeError('Password should have a password')
        user = self.create_user(username , email , password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255, unique=True, db_index=True)
    email=models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified =models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    is_superuser =models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username']

    objects =UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refreshToken=RefreshToken.for_user(self)
        return {
            'refresh': str(refreshToken),
            'access': str(refreshToken.access_token)
        }

    

class RegisterUser(models.Model):
    first_name = models.CharField(max_length=60)
    middle_name =models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=70,unique=True)
    email = models.EmailField(max_length=255 ,default='')
    phone =models.CharField(max_length=50)
    password =models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)


