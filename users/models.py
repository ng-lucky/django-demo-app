from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import dispatcher, receiver
# from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import datetime
# Create your models here.

class OKUserManager(BaseUserManager):
    # This method accepts basic information and create user
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have a email')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class OKUser(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(verbose_name='Email address', unique=True, max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    
    # auth_token
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = OKUserManager()
    
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        ordering = ('id', 'first_name',)

    def update_last_login(self):
        self.last_login_time = timezone.now()
        self.save()

@receiver(post_save, sender=OKUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    
    
    