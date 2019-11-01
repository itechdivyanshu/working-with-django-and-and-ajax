from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{"name":"ItechIndrutries"})

def add(request):
    try:
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        data= val1+val2
    except:
        data ="enter a integer not a string"
    return render(request,'home.html',{"name":"ItechIndrutries","data":data})

def index(request):
    return render(request,'index.html')

def sendajax(request):
    if request.method == 'POST':
        try:
            val1 = int(request.POST['num1'])
            val2 = int(request.POST['num2'])
            data= val1+val2
        except:
            data ="enter a integer not a string"
        return HttpResponse(data)