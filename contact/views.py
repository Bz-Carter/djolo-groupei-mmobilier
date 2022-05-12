from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail

from contact.serializers import ContactSerailizer


@api_view(['POST', ])
def contact(request):
    if request.method == "POST":
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # send mail
            # send_mail(
            #     name,
            #     subject,
            #     message,
            #     email,
            #     ['lebz2016@gmail.com'],
            # )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

