from django.urls import path
from .views import ContactDetail, ContactList

app_name = "contacts"
urlpatterns = [
    path("", ContactList.as_view(), name="contact-list"),
    path("<int:id>/", ContactDetail.as_view(), name="contact-detail"),
]
