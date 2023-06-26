import  uuid

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from cloudinary.models import CloudinaryField

from common.global_choices import USER_LEVEL, USER_TYPE
from core.model_mixins import AddressFields, AuditFields
from core.utils import randcode_gen

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
PHONE_NUMBER_REGEX = '^[ 0-9]+$'


class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, fullname, email, password, phone_number=None):
        if not email:
            raise ValueError('Users must have a valid Email Address.')
        if not username:
            username = self.normalize_email(email) 
        user = self.model(username = username, email = self.normalize_email(email), fullname = fullname,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password, username=None, phone_number=None):
        if not username:
            username = self.normalize_email(email)
        super_user = self.create_user(fullname = fullname, password = password, username = username, email = self.normalize_email(email),)
        super_user.user_type = 1
        super_user.user_level = 5
        super_user.is_active = True
        super_user.is_staff = True
        super_user.is_admin = True
        super_user.is_superuser = True
        super_user.save(using=self._db)
        return super_user

class CustomUser(AddressFields, AuditFields, AbstractBaseUser, PermissionsMixin):
    uuid_code = models.UUIDField('UUID CODE', primary_key=True, default=uuid.uuid4, editable=False)
    token_key = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False, blank=True, null=True)
    code = models.CharField('CODE', max_length=100, blank=False, default=randcode_gen)
    username = models.CharField('USERNAME', max_length=100, validators=[RegexValidator(regex=USERNAME_REGEX, message='Username must be alphanumeric or contains numbers.', code='invalid_username')], unique=True)
    phone_number = models.CharField('PHONE NUMBER', max_length=30, validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)
    country_code = models.CharField('COUNTRY CODE', max_length=5, blank=True, null=True)
    fullname = models.CharField('FULLNAME', max_length=100, blank=True, null=True)
    id_number = models.CharField('PASSPORT NUMBER', max_length=100, blank=True, null=True)
    dob = models.DateField(verbose_name="Date of Birth (DOB)", null=True, blank=True)
    birth_place = models.CharField('BIRTH PLACE', max_length=200, blank=True, null=True)
    email = models.EmailField('EMAIL', unique=True, blank=True, null=True)
    image = CloudinaryField('image', null=False, blank=True)
    user_type = models.PositiveSmallIntegerField('USER TYPE', default=3, choices=USER_TYPE)
    user_level = models.PositiveSmallIntegerField('USER LEVEL', default=1, choices=USER_LEVEL)
    last_login = models.DateTimeField('TIME LAST LOGIN', auto_now=True)
    is_active = models.BooleanField('IS ACTIVE CHECK', default=False)
    is_staff = models.BooleanField('IS STAFF CHECK', default=False)
    is_admin = models.BooleanField('IS ADMIN CHECK', default=False)
    is_superuser = models.BooleanField('IS SUPERUSER CHECK', default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname']

    class Meta:
        app_label = 'account'
        db_table = 'account'
        verbose_name_plural = 'account'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
