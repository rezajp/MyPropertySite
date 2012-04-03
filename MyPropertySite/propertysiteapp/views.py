
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *
from MyPropertySite.propertysiteapp.forms import *


def create_agency(request):
    form = AgencyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AgencyForm()

    t = get_template('propertysiteapp/create_agency.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_agency(request):
  
    list_items = Agency.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('propertysiteapp/list_agency.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_agency(request, id):
    agency_instance = Agency.objects.get(id = id)

    t=get_template('propertysiteapp/view_agency.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_agency(request, id):

    agency_instance = Agency.objects.get(id=id)

    form = AgencyForm(request.POST or None, instance = agency_instance)

    if form.is_valid():
        form.save()

    t=get_template('propertysiteapp/edit_agency.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_property(request):
    form = PropertyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PropertyForm()

    t = get_template('propertysiteapp/create_property.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_property(request):
  
    list_items = Property.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('propertysiteapp/list_property.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_property(request, id):
    property_instance = Property.objects.get(id = id)

    t=get_template('propertysiteapp/view_property.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_property(request, id):

    property_instance = Property.objects.get(id=id)

    form = PropertyForm(request.POST or None, instance = property_instance)

    if form.is_valid():
        form.save()

    t=get_template('propertysiteapp/edit_property.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_propertytype(request):
    form = PropertyTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PropertyTypeForm()

    t = get_template('propertysiteapp/create_propertytype.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_propertytype(request):
  
    list_items = PropertyType.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('propertysiteapp/list_propertytype.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_propertytype(request, id):
    propertytype_instance = PropertyType.objects.get(id = id)

    t=get_template('propertysiteapp/view_propertytype.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_propertytype(request, id):

    propertytype_instance = PropertyType.objects.get(id=id)

    form = PropertyTypeForm(request.POST or None, instance = propertytype_instance)

    if form.is_valid():
        form.save()

    t=get_template('propertysiteapp/edit_propertytype.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_sale(request):
    form = SaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SaleForm()

    t = get_template('propertysiteapp/create_sale.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_sale(request):
  
    list_items = Sale.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('propertysiteapp/list_sale.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_sale(request, id):
    sale_instance = Sale.objects.get(id = id)

    t=get_template('propertysiteapp/view_sale.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_sale(request, id):

    sale_instance = Sale.objects.get(id=id)

    form = SaleForm(request.POST or None, instance = sale_instance)

    if form.is_valid():
        form.save()

    t=get_template('propertysiteapp/edit_sale.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_rent(request):
    form = RentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RentForm()

    t = get_template('propertysiteapp/create_rent.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_rent(request):
  
    list_items = Rent.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('propertysiteapp/list_rent.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_rent(request, id):
    rent_instance = Rent.objects.get(id = id)

    t=get_template('propertysiteapp/view_rent.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_rent(request, id):

    rent_instance = Rent.objects.get(id=id)

    form = RentForm(request.POST or None, instance = rent_instance)

    if form.is_valid():
        form.save()

    t=get_template('propertysiteapp/edit_rent.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
