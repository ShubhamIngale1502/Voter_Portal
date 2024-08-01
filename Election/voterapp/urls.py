from django.urls import path
from .views import create,show_Details,update_Details,delete_Details,candidate_details

urlpatterns = [
    path('create/', create, name='create'),
    path('candidate/<int:pk>/',candidate_details, name="candidate" ),
    path('show/', show_Details, name='show'),
    path('update_details/<int:pk>/', update_Details, name='update'),
    path('delete_details/<int:pk>/', delete_Details, name='delete'),
]
