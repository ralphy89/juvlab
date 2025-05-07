from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('add_students', views.add_students, name='add-students'),
    path('view_students', views.view_students, name='view-students'),
    path('update_students/<int:pk>', views.update_students, name='update-students'),
    path('change_p_status/<int:pk>', views.change_participant_status, name='change-p-status'),
]