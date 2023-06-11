from django.shortcuts import render,redirect
from .models import Staff,Shift
# Create your views here.

def index(request):
    shifts = Shift.objects.all()
    return render(request,'index.html',{"shifts":shifts})

def make_entries(request):
    date = request.POST.get('date')
    shift = request.POST.get('shift')
    print(shift,date)
    return redirect('entry')

def entry(request):
    staffs = Staff.objects.all()
    return render(request,'entry.html',{'staffs':staffs})

def entry_action(request):
    
    return redirect('entry')

def dashboard(request):

    return render(request,'dashboard.html')

def error(request):

    return render(request,'error.html')