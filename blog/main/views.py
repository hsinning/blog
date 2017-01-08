from django.shortcuts import render
import datetime


def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很棒','now':now}
    
    if now.hour >= 6 and now.hour < 12 :
        context.update({'greeting': "morning"})
    elif now.hour >= 12:
        context.update({'greeting': "afternoon"})
    return render(request,'main/main.html',context)

def about(request):
    '''
    Render the about page
    '''
    return render(request,'main/about.html')
# Create your views here.
