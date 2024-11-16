import os

serializer_template = """from rest_framework import serializers
from .models import {ModelName}

class {ModelName}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {ModelName}
        fields = '__all__'
"""

def generate_serializer(module_name, model_name):
    directory = f'../backend/medical_system/serializers/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, f'{module_name}_serializers.py'), 'w') as file:
        file.write(serializer_template.format(ModelName=model_name))

if __name__ == "__main__":
    module_name = input("Enter the module name: ")
    model_name = input("Enter the model name: ")
    generate_serializer(module_name, model_name)
    print(f"Serializer for {model_name} generated successfully in {module_name}_serializers.py")
