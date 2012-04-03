
from django import forms
from models import *



class AgencyForm(forms.ModelForm):
	
    class Meta:
        model = Agency	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(AgencyForm, self).__init__(*args, **kwargs)



class PropertyForm(forms.ModelForm):
	
    class Meta:
        model = Property	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)



class PropertyTypeForm(forms.ModelForm):
	
    class Meta:
        model = PropertyType	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(PropertyTypeForm, self).__init__(*args, **kwargs)



class SaleForm(forms.ModelForm):
	
    class Meta:
        model = Sale	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)



class RentForm(forms.ModelForm):
	
    class Meta:
        model = Rent	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)

