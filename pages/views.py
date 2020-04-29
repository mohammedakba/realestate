from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm, Upload_property
from .models import Uploadproperty
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import smtplib
from math import ceil


#   allProds = []
#     catprods =Uploadproperty.objects.all()
#     cats = {item['property_cat'] for item in catprods}
#     for cat in cats:
#         prod = Uploadproperty.objects.filter(property_cat=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])
#         properties = {'allProds':allProds}
#     return render(request, 'shop/index.html', params)


def index(request):
    properties = Uploadproperty.objects.all()
    return render(request, 'basics/index1.html', {'properties': properties})


def home(request):
    properties = Uploadproperty.objects.all()
    return render(request, 'basics/home.html', {'properties': properties})


def about(request):
    return render(request, 'basics/about.html')


def login(request):

    return render(request, 'basics/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, "account has been created to " + username)
            return redirect('login')

        else:
            form = UserRegistrationForm(request.POST)
            messages.error(
                request, '')
            return render(request, 'basics/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    form = UserRegistrationForm()
    return render(request, 'basics/register.html', {'form': form})


@login_required
def upload(request):

    if request.method == 'POST':
        form = Upload_property(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            messages.success(
                request, "Thank you.! your details has been updated")
            form = Upload_property()
            return render(request, 'basics/upload.html', {'form': form})
    else:
        form = Upload_property()
    return render(request, 'basics/upload.html', {'form': form})


@login_required
def myupload(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email

        properties = Uploadproperty.objects.filter(contact_email__exact=email)

    return render(request, 'basics/myupload.html', {'properties': properties})


def pview(request):
    if request.method == 'GET':
        # try:
        a = request.GET.get('id')
        property1 = Uploadproperty.objects.filter(id=a)
        return render(request, 'basics/pviews.html', {'properties': property1})
        # except Uploadproperty.DeosNotExist:
        #     notfound = f"{request.GET.get('search')}Not Found Kindly contact the administrator"
        #     return render(request, 'basics/pview.html', {'notfound': notfound})
        # except ValueError:
        #     notfound = f"{request.GET.get('search')}invalid entry"
        #     return render(request, 'basics/pview.html', {'notfound': notfound})
    return render(request, 'basics/pviews.html')


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phnumber = request.POST.get('phnumber')
        message = request.POST.get('message')
        emailnote = f"{username} {email} {phnumber} {message}"
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("divumeh100@gmail.com", "king@2020")
        message = f"Contact US Mail from Website {emailnote}"
        s.sendmail("divumeh100@gmail.com", "gurav2001siddu@gmail.com", message)
        s.quit()

        messages.success(
            request, "Thank you for reporting")
        return render(request, 'basics/contact.html')

    return render(request, 'basics/contact.html')


def search(request):
    if request.method == 'POST':
        a = request.POST.get('search')

        property1 = Uploadproperty.objects.filter(
            Q(property_type__icontains=a) | Q(project_name__icontains=a) | Q(price__icontains=a))
        print(property1)
        return render(request, 'basics/home.html', {'properties': property1})
    return render(request, 'basics/home.html')

# editing the user properties


def edit(request):

    if request.POST.get('editedid') != None:
        id = request.POST.get('editedid')
        instance = Uploadproperty.objects.get(id=id)
        form = Upload_property(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            email = request.user.email
            messages.success(
                request, "your changes has saved")
            properties = Uploadproperty.objects.filter(
                contact_email__exact=email)
            return render(request, 'basics/myupload.html', {'properties': properties})

    id = request.POST.get('id')
    id = Uploadproperty.objects.get(id=id)
    form = Upload_property(instance=id)

    return render(request, 'basics/edit.html', {'form': form, 'id': id})


def delete(request):
    if request.method == "POST":

        id = request.POST.get('id')
        Uploadproperty.objects.get(id=id).delete()
        messages.error(request, " property has deleted")
        email = request.user.email
        properties = Uploadproperty.objects.filter(contact_email__exact=email)
        return render(request, 'basics/myupload.html', {'properties': properties})

    email = None
    if request.user.is_authenticated:
        email = request.user.email
        properties = Uploadproperty.objects.filter(contact_email__exact=email)
    return render(request, 'basics/myupload.html', {'properties': properties})
