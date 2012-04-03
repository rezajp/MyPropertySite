from django.template import Context
from MyPropertySite.propertysiteapp.models import Advertisement, Rent
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
    properties=Rent.objects.all()
    if(properties.count() > 0):
        paginator= Paginator(properties, 20, 0, False)
        page=paginator.page(1)
        variables = Context({
            'properties': page.object_list,
            'has_next': page.has_next(),
            'has_previous': page.has_previous(),
            'num_of_pages':paginator.num_pages,
            'count':paginator.count
        })
    else:
        variables = Context({
            'properties': properties,
            'has_next': False,
            'has_previous': False,
            'num_of_pages':0,
            'count':0
        })
    return render_to_response('home.html',variables)

def detail(request,ad_id):
    ad = get_object_or_404(Advertisement, pk=ad_id)
    return render_to_response('ads/detail.html', {'ad': ad})
def new_rent(request):
	if(request.method=='GET'):
		return render_to_response('ads/newrent.html')
	elif(request.method=='POST'):
		posted = request.POST
		r= Rent()
		p= Property()
		p.address_line1= posted["address_line1"]
		P.address_line2= posted["address_line2"]
		p.town=posted["town"]
		p.country=posted["country"]
		p.post_code=posted["post_code"]
		#longitude= models.DecimalField(decimal_places=10,max_digits=20)
		#latitude =models.DecimalField(decimal_places=10,max_digits=20)
		p.type_of_property = PropertyType.get(pk=posted["type_of_property"])
		p.no_of_bedrooms=posted["no_of_bedrooms"]
		p.no_of_bathrooms=posted["no_of_bathrooms"]
		#agency = models.ForeignKey('Agency', null=False,related_name='properties')
		p.save()
		r.for_property = p
		r.description= posted["description"]
		r.slot_start=posted["slot_start"]
		r.slot_end= posted["slot_end"]
		#rent.created_at= 
		r.rent = posted["rent"]
		r.deposit= posted["deposit"]
		r.available_on= posted["available_on"]
		r.save()
		return render_to_response('ads/detail.html',{'ad',r})
		
		
def ad_edit(request,ad_id):
    ad= get_object_or_404(Advertisement, pk=ad_id)
    if(request.method == 'GET'):
        if(isinstance(ad,'RentAdvertisement')):
            return render_to_response('ads/rent_ad_edit.html',{'ad',ad})
        elif(isinstance(ad,'SaleAdvertisement')):
            return render_to_response('ads/sale_ad_edit.html',{'ad',ad})
    elif(request.method=='POST'):
        if(isinstance(ad,'RentAdvertisement')):
            #update the add from request
            return render_to_response('ads/detail.html',{'ad',ad})
        elif(isinstance(ad,'SaleAdvertisement')):
            #update the add from request
            return render_to_response('ads/detail.html',{'ad',ad})
        
