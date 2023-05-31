from django import forms
from myApp.models import blogModel, portfolioModel

class blogForm(forms.ModelForm):
    class Meta:
        model = blogModel
        fields = ['titre', 'image', 'description']

class portfolioForm(forms.ModelForm):
    class Meta:
        model = portfolioModel
        fields = ['titre', 'description']