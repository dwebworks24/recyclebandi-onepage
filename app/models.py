from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations =True
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not phone:
            raise ValueError("Phone number is required")

        # Normalize email address
        email = self.normalize_email(email)

        # Create and save the user with required fields
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        # Create a superuser with required fields and additional permissions
        user = self.create_user(email, username, phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

user_roles = (
        ('admin', 'admin'),
        ('cluster', 'cluster'),
        ('customer','customer'),
    )

    
class Users(AbstractBaseUser, PermissionsMixin):
    # Custom user model fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    referal_code  = models.CharField(max_length=100,blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Required for custom user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define the field to be used as the unique identifier for logging in
    USERNAME_FIELD = 'email'
    # Additional fields required when creating a user
    REQUIRED_FIELDS = ['username', 'phone']

    # Custom user manager
    objects = UserManager()

    role = models.CharField(choices=user_roles,max_length=100,null=True,blank=True,default='admin')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
         return True

