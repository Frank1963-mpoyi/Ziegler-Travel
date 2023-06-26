from django.db.models import Q

from hospital.apps.web.home.models import Doctor


def get_doctors(self):
    
    doctor = Doctor.objects \
        .exclude(
        Q(bool_deleted=True)
    ).values('code', 'name', 'image', 'gender', 'phone_number', 'datetime_created', 'publish', 'whatsapp_number',
            'dob', 'department') \
        .order_by('-datetime_created')
        
    return doctor
