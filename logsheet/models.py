import uuid
#from PIL import Image
from django.contrib.auth import get_user_model
#from django.db.models.signals import pre_save, post_save
from django.db import models
#from datetime import datetime

from cloudinary.models import CloudinaryField

from common import global_choices as common_choice
from core.model_mixins import   AuditFields
from core import utils as common_utils

User = get_user_model()


# Create your models here.
class DriverLogsheet(AuditFields):
    code = models.CharField('CODE', max_length=100, blank=False, default=common_utils.randcode_gen)
    token_key = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False, blank=True, null=True)
    
    driver_name = models.CharField('FULL NAME', max_length=250)
    vehicule_type = models.CharField('VEHICULE TYPE', max_length=150)
    time_in = models.CharField('TIME IN', max_length=50)
    time_out = models.CharField('TIME OUT', max_length=50)
    km_in = models.CharField('KM IN', max_length=50)
    km_out = models.CharField('KM OUT', max_length=50)
    destination = models.CharField('DESTINATION', max_length=500)
    voucher_number = models.CharField('VOUCHER NUMBER', max_length=500)
    cost = models.CharField('COST', max_length=500)
    note = models.CharField('NOTE', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.driver_name