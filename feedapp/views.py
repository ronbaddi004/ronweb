from __future__ import unicode_literals
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from .models import Feedbaack
from django.core.urlresolvers import reverse

def first(request):
    return render(request, 'feedapp/index.html', {})


def second(request):
    return render(request, 'feedapp/port2.html', {})

def third(request):
    return render(request, 'feedapp/port3.html', {})

def forth(request):
    return render(request, 'feedapp/port4.html', {})

def success(request):
    return render(request, 'feedapp/success.html', {})


def get_ip(request):
    try:
        x_forward = request.META.get("HTML_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ""
    return ip

def Home(request):
    print(request.META.get('REMOTE_ADDR'))
    form = ContactForm(request.POST or None)
    if form.is_valid():
        new_sub = form.save(commit=False)
        contactName = form.cleaned_data['contactName']
        contactEmail = form.cleaned_data['contactEmail']
        contactSubject = form.cleaned_data['contactSubject']
        contactMessage = form.cleaned_data['contactMessage']
        new_old, created = Feedbaack.objects.get_or_create(contactName=contactName,contactEmail=contactEmail,contactSubject=contactSubject,contactMessage=contactMessage)
        if created:
            new_old.ip_add = get_ip(request)
            new_old.save()
            # return redirect('index')
        
        # contact_name = request.POST.get('contact_name', '')
        # contact_email = request.POST.get('contact_email', '')
        # form_content = request.POST.get('content', '')
        # template = get_template('contact_temp.txt')

        # context = {
        #     'contact_name': contact_name,
        #     'contact_email': contact_email,
        #     'form_content': form_content,
        # }
        # content = template.render(context)

        # email = EmailMessage(
        #     "New contact form submission",
        #     content,
        #     "pydj" +'',
        #     ['ronbaddi004@gmail.com'],
        #     headers = {'Reply-To': contact_email }
        # )

        # email.send()
        # return redirect('contact')

    return render(request, 'feedapp/home.html', {
        'form': form,
    })