from django.shortcuts import render

# Create your views here.


def mdbootstrap(request):
    return render(request,'mdbootstrap.html')

def child(request):
    return render(request,'child.html')
