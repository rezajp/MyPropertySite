from django.http import HttpRequest
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from MyPropertySite.properysiteapp.models import PropertyAdvertisement
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
    properties=PropertyAdvertisement.objects.all()
    paginator= Paginator(properties, 20, 0, False)
    page=paginator.page(1)
    variables = Context({
       'properties': page.object_list,
       'has_next': page.has_next(),
       'has_previous': page.has_previous(),
        'num_of_pages':paginator.num_pages,
        'count':paginator.count
    })
    return render_to_response('home.html',variables)

def detail(request,ad_id):
    ad = get_object_or_404(PropertyAdvertisement, pk=ad_id)
    return render_to_response('ads/detail.html', {'ad': ad})


