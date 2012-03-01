from django.http import HttpRequest
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from MyPropertySite.properysiteapp.models import PropertyAdvertisement
from django.core.paginator import Paginator

def home(request):
    template = get_template('home.html')
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
    
    output = template.render(variables)
    return HttpResponse(output)
