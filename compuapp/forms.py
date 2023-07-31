from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
   class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address','operating_system', 'users_name', 'location', 'purchase_date']

   def clean_computer_name(self):  # Validates the Computer Name Field
       computer_name = self.cleaned_data.get('computer_name')
       if (computer_name == ""):
           raise forms.ValidationError('Este campo no puede quedar vacio.')

       for instance in Computer.objects.all():
           if instance.computer_name == computer_name:
              raise forms.ValidationError('El nombre ' + computer_name + ' ya existe.')

       return computer_name

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name','users_name']


