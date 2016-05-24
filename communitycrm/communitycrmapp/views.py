from django.shortcuts import render

from .forms import MemberForm
# Create your views here.

def home(request):
    return render(request, 'communitycrmapp/home.html', {})

def add(request):
    return render(request, 'communitycrmapp/add.html', {})

def post_new(request):
    form = MemberForm()
    return render(request, 'communitycrmapp/new.html', {'form': form})
