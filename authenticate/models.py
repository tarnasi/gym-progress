import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

from rest_framework_simplejwt.tokens import RefreshToken

from .utils import user_avatars


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValidationError({'Email': ['Email is Required.']})

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValidationError({'Password': ['Password is Required.']})

        admin = self.create_user(
            email=self.normalize_email(email)
        )

        admin.set_password(password)

        admin.is_active = True
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_admin = True
        admin.is_email_verified = True
        admin.email_verify_at = datetime.now()
        admin.save(using=self._db)
        return admin


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='Email', max_length=65, unique=True, blank=False, null=False)
    last_login = models.DateTimeField(verbose_name='Update at', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    email_verify_at = models.DateTimeField(verbose_name='Email verification date', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=user_avatars, blank=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        data = {
            'refresh': str(token),
            'access': str(token.access_token)
        }
        return data

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('date_joined',)


class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.PositiveBigIntegerField(default=0, blank=True)
    height = models.FloatField(default=0.0, blank=True)
    blood_type = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f"User {self.user.email} info: {self.blood_type}"

    class Meta:
        verbose_name = 'personal_info'
        verbose_name_plural = 'PersonalInfo'
        ordering = ('weight',)
