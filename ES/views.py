from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse

# Create your views here.
def Home(request):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        send_mail(
            'Hello Krunal',
            'Hello from himanish ------"HI"',
            'himanishvyas.tecblic@gmail.com',  
            ['himanisih.vyas@gmail.com'], 
            
            fail_silently=False,
        )
        print("/////////////////////////////////////////")
        return HttpResponse("Mail Sent!!")