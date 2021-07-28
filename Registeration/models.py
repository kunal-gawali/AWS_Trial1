from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
#from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email')
        if not username:
            raise ValueError('Users must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.deactivated = False
        user.save(using=self._db)
        return user

# Modified django built-in 'User' model
# Authentication: Email and Password
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=80, unique=True)  # Mandatory
    username = models.CharField(
        max_length=30, blank=True, null=True)
    
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    deactivated = models.BooleanField(default=False)

    # For first time registration authentication
    registration_authenticated = models.BooleanField(default=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def _str_(self):
        return str(self.id) + ' ' + self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def set_username(self):
        if self.phone:
            self.username = self.full_name[:1:] + self.phone
        else:
            self.username = self.full_name[:1:]
        self.save()

class JsonTab(models.Model):
    BALANCE = models.CharField(max_length=200, blank=True, null=True)
    NARRATION = models.CharField(max_length=200, blank=True, null=True)
    TRANSACTION_DATE = models.CharField(max_length=200, blank=True, null=True)
    month = models.CharField(max_length=200, blank=True, null=True)
    transactionAmount = models.CharField(max_length=200, blank=True, null=True)
    transactionPrimaryCategory = models.CharField(max_length=200, blank=True, null=True)
    transactionSecondaryCategory = models.CharField(max_length=200, blank=True, null=True)
    transactionType = models.CharField(max_length=200, blank=True, null=True)