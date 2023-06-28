
from django.urls import path

from .views import (
    create_driver_logsheet,
    update_driver_logsheet,
    delete_driver_logsheet,
    logsheet_list_view,
    logsheet_list_view,
)


urlpatterns = [
    path('', logsheet_list_view, name='list-logsheet'),
    path('logsheet/create/', create_driver_logsheet, name='logsheet_create'),
    path('logsheet/<int:pk>/update/', update_driver_logsheet, name='logsheet_update'),
    path('logsheet/<int:pk>/delete/', delete_driver_logsheet, name='logsheet_delete'),
    path('logsheet/<int:pk>/', logsheet_list_view, name='logsheet_detail'),
] 