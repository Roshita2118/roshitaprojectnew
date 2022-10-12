from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from .forms import GeeksForm
from django.contrib import admin
from .models import GeeksModel
def index(request):
   return HttpResponse("Hello Geeks")

# Create your views here.
#def home_view(request):
#	return render(request, "home.html")


from django.shortcuts import render


def home_view(request):
    context = {}

    # create object of form
    form = GeeksForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "home.html", context)


from .forms import GeeksForm

# importing formset_factory
from django.forms import formset_factory


def formset_view(request):
    context = {}

    # creating a formset
    GeeksFormSet = formset_factory(GeeksForm, extra =5)
    formset = GeeksFormSet()

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "home.html", context)

def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "home.html", context)



def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


from .models import GeeksModel


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)


from django.urls import path


from .models import GeeksModel


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)

    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


from django.http import HttpResponse
from django.views import View


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


from django.views.generic.edit import CreateView
from .models import GeeksModel

class GeeksCreate(CreateView):
    # specify the model for create view
    model = GeeksModel

    # specify the fields to be displayed

    fields = ['title', 'description']