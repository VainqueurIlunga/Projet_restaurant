from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save

#  Custom User Manager
class UserManager(BaseUserManager):

    def create_user(self, email, name, tc,user_type, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError('Email can not be null.')
        email = self.normalize_email(email)
        user = self.model(email=email,
                            name=name,
                            tc=tc,
                            user_type=user_type,
                            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    

    def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
          user_type=1
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
    
    GENDER = [("M", "Male"), ("F", "Female")]
    STATUS = [("Actif", "actif"), ("Inactif", "inactif")]
    USER_TYPE = ((1, "admin"),  (2, "client"),(3, "vendor"))
    #username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,)
    firstname = models.CharField(max_length=255, db_index=True)
    lastname = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=15, null=True, unique=True)
    gender = models.CharField(max_length=67)
    address = models.TextField()
    city = models.CharField(max_length=255, db_index=True)
    state = models.CharField(max_length=255, db_index=True)
    postal_code = models.CharField(max_length=255, db_index=True)
    country = models.CharField(max_length=255, db_index=True)
    profile_image = models.ImageField(upload_to='profile/',default="user.png")
    user_type = models.CharField(default=1, max_length=1)
    # the token session
    
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Client(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.email + ", " + self.admin.firstname
    

class Employer(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.email + ", " + self.admin.firstname
    
class EmployerAdmin(Employer):
    #admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.email + ", " + self.admin.firstname


class Vendor(Employer):
    # role = models.CharField(max_length=30)
    
    def __str__(self):
        return self.admin.lastname + ", " + self.admin.firstname


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            EmployerAdmin.objects.create(admin=instance)
        if instance.user_type == 2:
            Vendor.objects.create(admin=instance)
        if instance.user_type == 3:
            Client.objects.create(admin=instance)   
       
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.employer.save()
    if instance.user_type == 2:
        instance.employer.save()
    if instance.user_type == 3:
        instance.client.save()
   



