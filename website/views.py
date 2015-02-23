from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import TemplateView
from django.core.mail import send_mail

def signup(request):
    try:
        d = request.POST
        andrew_id = d.get("andrew_id")
        name = d.get("name")
        subject = "D-List Request"
        message = "Andrew ID: {}\nName: {}\n".format(andrew_id, name)
        from_email = "robertmaratos@gmail.com"
        recipient_list = ["rmaratos@andrew.cmu.edu"]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse(andrew_id + " Successfully Added")
    except Exception as e:
        return HttpResponseBadRequest(e)


