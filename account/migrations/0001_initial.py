# Generated by Django 4.2.2 on 2023-06-26 09:12

import cloudinary.models
import core.utils
import django.core.validators
from django.db import migrations, models
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('street_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street Name')),
                ('house_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number')),
                ('post_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Postal Code')),
                ('area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Area')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='DATE UPDATED')),
                ('time_updated', models.TimeField(blank=True, null=True, verbose_name='TIME UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('publish', models.DateField(blank=True, null=True)),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID CODE')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=core.utils.randcode_gen, max_length=100, verbose_name='CODE')),
                ('username', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contains numbers.', regex='^[a-zA-Z0-9.+-]*$')], verbose_name='USERNAME')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Invalid Phone Number', regex='^[ 0-9]+$')], verbose_name='PHONE NUMBER')),
                ('country_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='COUNTRY CODE')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True, verbose_name='FULLNAME')),
                ('id_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='PASSPORT NUMBER')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth (DOB)')),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True, verbose_name='BIRTH PLACE')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='EMAIL')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'MPT Systems'), (2, 'HP Staff'), (3, 'Customer')], default=3, verbose_name='USER TYPE')),
                ('user_level', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, verbose_name='USER LEVEL')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='TIME LAST LOGIN')),
                ('is_active', models.BooleanField(default=False, verbose_name='IS ACTIVE CHECK')),
                ('is_staff', models.BooleanField(default=False, verbose_name='IS STAFF CHECK')),
                ('is_admin', models.BooleanField(default=False, verbose_name='IS ADMIN CHECK')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='IS SUPERUSER CHECK')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'account',
                'db_table': 'account',
            },
        ),
    ]
