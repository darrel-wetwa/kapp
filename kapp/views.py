from django.shortcuts import render
from kapp.models import Member

# Create your views here.
def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request,'inner-page.html')



def portfolio(request):
    return render(request,'portfolio-details.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        member.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'LOG IN.html')
