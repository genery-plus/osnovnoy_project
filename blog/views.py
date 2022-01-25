"""#страница abc 
def saveforms (request):
    form = CharacterForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        a = form.save(commit=False)
        a.save()
        return redirect("saveforms")
    return render(request,"./main.html", {'form': form})"""
from django.shortcuts import render, redirect
from .models import character
from .forms import CharacterForm
from django.views.decorators.csrf import csrf_exempt


#страница abc 
@csrf_exempt
def saveforms (request):
    form = CharacterForm(request.POST or None)
    if request.method=="POST":
        a = form.save(commit=False)
        a.save()
        return redirect("saveforms")
    return render(request,"./main.html", {'form': form})
#основная страница
def index (request):
    return  render(request,"index.html",{})

#страница main
def main (request):
    return  render(request,"main.html",{})

def page_choice (request):
    return render(request,"page_choice.html",{})