# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactMe


def index(request):
    # render(request, template name, optional dictionary)
    return render(request, 'notary/base.html')
    #return HttpResponse("Hello world")

def get_name(request):
    if request.method == "POST":
        # create a form instance & populate it with date from the request
        form = ContactMe(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            sender = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ["Nineteen99@gmail.com"]

            message = name + "\n\n" + message + "\n\n" + address + ", " + city + "\n\n" + sender

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)

            # redirect to new url
            return HttpResponseRedirect('notary/thanks/')

    # if GET we'll create a blank form
    else:
        form = ContactMe()

    return render(request, 'notary/form.html', {'form': form})

def thanks(request):
    return render(request, 'notary/thanks.html')
