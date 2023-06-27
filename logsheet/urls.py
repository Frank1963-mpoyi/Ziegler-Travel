
from django.urls import path
from .views import logsheet_list_view #, create_logsheet

urlpatterns = [
    path('', logsheet_list_view, name='list-logsheet'),

] 
