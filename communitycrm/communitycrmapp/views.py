from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from .forms import MemberForm
from .models import Member
from django.core.exceptions import *

# Create your views here.

def home(request):
    return render(request, 'communitycrmapp/home.html', {})

def searchpage(request):
    return render(request, 'communitycrmapp/searchpage.html', {})

def new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'communitycrmapp/success.html', {'form': form})
    else:
        form = MemberForm()
    return render(request, 'communitycrmapp/new.html', {'form': form})

def display(request):
    members = Member.objects.all()
    return render(request, 'communitycrmapp/display.html', {
        'members': members
    })

def search_by_name(request):
    if request.method == "POST":
        search_id = request.POST.get('namequery')
        try:
            member_by_name = Member.objects.filter(name__icontains= search_id)
            print(member_by_name)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_name': member_by_name})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')


def member_item(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'communitycrmapp/member.html', {
        'member': member
    })
