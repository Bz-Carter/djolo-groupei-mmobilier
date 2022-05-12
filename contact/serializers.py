from rest_framework import serializers
from django.core.mail import send_mail
class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()
    def create(self, validate_data):
        instance = super(ContactSerailizer, self).create(validate_data)
        send_mail(
            'Instance {} has been created'.format(instance.pk),
            'Here is the message. DATA: {}'.format(validate_data),
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return instance
