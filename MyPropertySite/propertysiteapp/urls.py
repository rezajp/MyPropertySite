
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'agency/create/$', create_agency),
    (r'agency/list/$', list_agency ),
    (r'agency/edit/(?P<id>[^/]+)/$', edit_agency),
    (r'agency/view/(?P<id>[^/]+)/$', view_agency),
    
    (r'property/create/$', create_property),
    (r'property/list/$', list_property ),
    (r'property/edit/(?P<id>[^/]+)/$', edit_property),
    (r'property/view/(?P<id>[^/]+)/$', view_property),
    
    (r'propertytype/create/$', create_propertytype),
    (r'propertytype/list/$', list_propertytype ),
    (r'propertytype/edit/(?P<id>[^/]+)/$', edit_propertytype),
    (r'propertytype/view/(?P<id>[^/]+)/$', view_propertytype),
    
    (r'sale/create/$', create_sale),
    (r'sale/list/$', list_sale ),
    (r'sale/edit/(?P<id>[^/]+)/$', edit_sale),
    (r'sale/view/(?P<id>[^/]+)/$', view_sale),
    
    (r'rent/create/$', create_rent),
    (r'rent/list/$', list_rent ),
    (r'rent/edit/(?P<id>[^/]+)/$', edit_rent),
    (r'rent/view/(?P<id>[^/]+)/$', view_rent),
    
)
