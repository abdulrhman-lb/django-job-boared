from django import forms
from .models import Apply 
from job.models import job


class ApplyForm(forms.ModelForm):
    
    class Meta:
        model = Apply
        fields = ("name", "email", "website", "cv", "cover_letter")



class AddForm(forms.ModelForm):
    
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner' , 'slug' , )

