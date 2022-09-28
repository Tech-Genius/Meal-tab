from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from . models import *
from django.db.models import Q
from shop.models import Product
from django.core.mail import send_mail
from meal_tab import settings 
# Create your views here.


# HOME

def home(request):
    promos = Product.objects.filter(has_discount=True)
    populars = Product.objects.filter(is_featured=True)
    breakfasts = Breakfast.objects.all()
    lunchs = Lunch.objects.all()
    dinners = Dinner.objects.all()
    chefs = Chef.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_message = request.POST['user_message']
        message = "Hello, \n" + ' ' + '\n' + name + " just filled out the contact us form, you can get in touch with " + name + " through the details he provided below if there's a need.\n " + ' ' + '\n' + "Name: " + name + '\n' + "Email: " +  email + '\n' + "Phone Number: " +  phone  + '\n' + name + " 's Message: " + user_message  
        subject = "New Contact Form Entry From " + name
        send_mail(
            subject,
            message,
            email,
            ['adebimpehabeeb10@gmail.com'],
            fail_silently=False

        )

        context = {
        'promos' : promos, 
        'populars' : populars,
        'breakfasts': breakfasts, 
        'lunchs': lunchs,
        'dinners':dinners,
        'chefs' : chefs,
        'name': name,
        'user_message':user_message 
        }

        return render(request, 'index.html', context)
    else:
        context = {
        'promos' : promos, 
        'populars' : populars,
        'breakfasts': breakfasts, 
        'lunchs': lunchs,
        'dinners':dinners,
        'chefs' : chefs,
         }
        return render(request, 'index.html', context)    


# search

def search(request):

    if request.method == 'GET':
        q = request.GET['q']
        results = Product.objects.filter(Q(title__icontains=q) | Q(category__title__icontains=q)).distinct()
        context = {'q': q, 'results': results}
        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html', {}) 




# event reservation

def event_reservation(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        guests = request.POST['guests']
        address = request.POST['address']
        all_messages = "Hello, \n" + ' ' + '\n' + message_name + " just filled out the event reservation notice form, you can get in touch with " + message_name + " through the details he provided below to start planning for the event.\n " + ' ' + '\n' + "Name: " + message_name + '\n' + "Email: " +  email + '\n' + "Phone Number: " +  phone  + '\n' + "Event Date: " + date + '\n' + "Amount Of Guests Expected: " + guests + '\n' + "Event Location: " + address 
        subject = 'New Event Reservation Form Entry, From ' + message_name 


        send_mail(
                subject,
                all_messages,
                email,
                ['adebimpehabeeb10@gmail.com'],
                fail_silently=False,
            )

        context = {
                'message_name': message_name,
                'email' : email,
                'phone': phone,
                'date' : date,
                'guests': guests

        }

        return render(request, 'event-reservation.html', context)




    else:
        return render (request, 'event-reservation.html', {})   




# tabe reservation

def table_reservation(request):

    if request.method == 'POST':
        message_name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        number_of_people = request.POST['number_of_people']
        all_messages = "Hello, \n" + ' ' + '\n' + message_name + " just filled out the table reservation notice form, you can get in touch with " + message_name + " through the details he provided below to start planning for the meal.\n " + ' ' + '\n' + "Name: " + message_name + '\n' + "Email: " +  email + '\n' + "Phone Number: " +  phone  + '\n' + "Date: " + date  + '\n' + "Time: " + time  + '\n' + "Amount Of People Coming: " + number_of_people 
        subject = 'New Table Reservation Form Entry, From ' + message_name 


        send_mail(
                subject,
                all_messages,
                email,
                ['adebimpehabeeb10@gmail.com'],
                fail_silently=False,
            )

        context = {
                'message_name': message_name,
                'email' : email,
                'phone': phone,
                'date' : date,
                'number_of_people': number_of_people,
                'time': time

        }

        return render(request, 'table-reservation.html', context)
    else:

        return render(request, 'table-reservation.html')




    