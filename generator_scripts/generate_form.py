import os

form_template = """from django import forms
from .models import {ModelName}

class {ModelName}Form(forms.ModelForm):
    class Meta:
        model = {ModelName}
        fields = '__all__'
"""

def generate_form(module_name, model_name):
    directory = f'../backend/medical_system/forms/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, f'{module_name}_forms.py'), 'w') as file:
        file.write(form_template.format(ModelName=model_name))

if __name__ == "__main__":
    module_name = input("Enter the module name: ")
    model_name = input("Enter the model name: ")
    generate_form(module_name, model_name)
    print(f"Form for {model_name} generated successfully in {module_name}_forms.py")
