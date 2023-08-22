from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
	return HttpResponse("Hello World!")
def index1(request):
	return HttpResponse("Django new project")
def htmlexample(request):
	template=loader.get_template("file.html")
	return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .forms import PetForm

def adoption_form(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adoption_form')
    else:
        form = PetForm()
    return render(request, 'adoptions/adoption_form.html', {'form': form})


def form(request):
	template=loader.get_template("adoption_form.html")
	return HttpResponse(template.render())