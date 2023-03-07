from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, user_name,email,phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(user_name,email,phone_number, password, **other_fields)

    def create_user(self,user_name, email,phone_number,  password, **other_fields):

        if not phone_number:
            raise ValueError(_('You must provide an email address or phone number'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True,null=True)
    phone_number=models.BigIntegerField(unique=True,null=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    last_payment = models.DateTimeField(blank=True,null=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    objectsDefault=models.Manager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email','phone_number']

    def clean(self):
        if not self.email or self.phone_number:
            raise ValidationError(
                {'required_field': ['This field is required when conditional_field is not null.']})

    def __str__(self):
        return self.user_name