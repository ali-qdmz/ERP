from django import forms
from project_management.models import *


class MovieChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    cutting = forms.ModelMultipleChoiceField(queryset=Cutting.objects.all(),
                                             required=False)
