from django.shortcuts import render
from .models import HomePageContent, Contact
from django.core.mail import send_mail


# Create your views here.
def index(request):
    contact = Contact.objects.all()
    logo = HomePageContent.objects.all()
    context = {'logo': logo, 'contact': contact}

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        locality = request.POST.get('locality')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(first_name=first_name, last_name=last_name, locality=locality, email=email, phone=phone)
        contact.save()


    return render(request, 'index.html', context)

