from django.urls import path
from .views import contacts, contactDetails

urlpatterns = [
    path('contacts/', contacts.as_view(), name='contact'),
    path('contacts/<int:pk>', contactDetails.as_view(), name='contact')
]