from django.shortcuts import render
import datetime

def contact(request):
    '''
    Render the contact page
    '''
    context={ 'now':datetime.datetime.now()}
    return render(request,'contact/contact.html',context)
