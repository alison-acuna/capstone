from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .forms import MemberForm
from .models import Member

# Create your views here.

def home(request):
    return render(request, 'communitycrmapp/home.html', {})

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

def member_item(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'communitycrmapp/member.html', {
        'member': member
    })

def search(request):
    query = request.GET.get('name')
    # try:
    #     query = int(query)
    #     # not sure about int(query) above
    # except ValueError:
    #     query = None
    #     results = None    
    if query:
        results = Member.objects.get(uid=query)
    context = RequestContext(request)
    return render(request, 'results.html', {
        "results": results
        }, context_instance=context)





    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'communitycrmapp/success.html', {'form': form})
    else:
        form = MemberForm()
    return render(request, 'communitycrmapp/search.html', {})
