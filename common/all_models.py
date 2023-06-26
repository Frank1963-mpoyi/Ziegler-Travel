# from hospital.apps.web.home.models import (
#     Comment, Contact, Doctor as Doctors, Patient, 
#     LatestNews, Product , PatientDischargeDetails, MakeAnAppointment , Staff 
#     )
    
    
# def query_all_models(self):
    
#     all_query = {
#         "comment": Comment.objects.all().values().count(),
#         "staff": Staff.objects.all().values().count(),
#         "contact": Contact.objects.all().values().count(),
#         "doctors": Doctors.objects.all().values().count(),
#         "patients": Patient.objects.all().values().count(),
#         "news": LatestNews.objects.all().values().count(),
#         "products":Product.objects.all().values().count(),
#         "patient_detail": PatientDischargeDetails.objects.all().values().count(),
#         "appointments": MakeAnAppointment.objects.all().values().count(),
#     }

#     return all_query