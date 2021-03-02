from django.contrib.auth import models
from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ["id", "firstname", "lastname", "phone_number",
                  "contact_picture", "is_favourite", "timestamp"]
