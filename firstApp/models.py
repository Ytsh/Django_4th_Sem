from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    enrollment_date = models.DateField(auto_now_add=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, related_name = 'students', null=True)
    def __str__(self): #This is two underscore not one
        return f"{self.first_name} {self.last_name}"



class Profile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profiles/')

    # For relation
    # One to one relation
    # models.OneToOneField()
    # for one to many
    # models.ForeignKey()
    # for many to meny
    # models.ManyToManyField()
    #college = models.ForeignKey(College, on_delete=models.CASCADE, related_name = 'students')

# try except raise

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
