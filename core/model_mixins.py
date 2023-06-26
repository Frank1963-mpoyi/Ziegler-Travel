from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
PHONE_NUMBER_REGEX = '^[ 0-9]+$'


class AddressFields(models.Model):
    street_name = models.CharField('Street Name', max_length=200, blank=True, null=True)
    house_number = models.PositiveSmallIntegerField('Number', blank=True, null=True)
    post_code = models.CharField('Postal Code', max_length=50, blank=True, null=True)
    area = models.CharField('Area', max_length=100, blank=True, null=True)
    city = models.CharField('City',max_length=100, blank=True, null=True)
    region = models.CharField('Region', max_length=100, blank=True, null=True)
    country = CountryField('Country', null=True)

    class Meta:
        abstract = True

class AuditFields(models.Model):
    datetime_created = models.DateTimeField('DATE CREATED', auto_now_add=True)
    datetime_updated = models.DateTimeField('DATE UPDATED', auto_now=True , null=True, blank=True)
    time_updated = models.TimeField("TIME UPDATED", null=True, blank=True)
    last_updated_by = models.CharField('LAST UPDATED BY', max_length=50, blank=True, null=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    bool_deleted = models.BooleanField('IS DELETED?', default=False)

    class Meta:
        abstract = True


class EmailFields(models.Model):
    email = models.EmailField('Email',blank=True, null=True)
    email1 = models.EmailField('Admin. Email',blank=True, null=True)
    email2 = models.EmailField('Account Email',blank=True, null=True)
    email3 = models.EmailField('Branch Email', blank=True, null=True)
    email4 = models.EmailField('Legal Email', blank=True, null=True)

    class Meta:
        abstract = True
        
class PhoneFields(models.Model):
    phone = models.CharField('Phone', max_length=30, unique=False, blank=False, null=False, default='xxxxxxxxxx')
    phone1 = models.CharField('Phone 1', max_length=30, unique=False, blank=True, null=True)
    phone2 = models.CharField('Phone 2', max_length=30, unique=True, blank=True, null=True)
    phone3 = models.CharField('Phone 3', max_length=30, unique=True, blank=True, null=True)
    phone4 = models.CharField('Phone 4', max_length=30, unique=True, blank=True, null=True)
    phone_number = models.CharField('PHONE NUMBER', max_length=30, validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)
    relative_phone_number = models.CharField('RELATIVE PHONE NUMBER', max_length=30, validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)
    whatsapp_number = models.CharField('PHONE NUMBER',max_length=30, validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)

    class Meta:
        abstract = True
