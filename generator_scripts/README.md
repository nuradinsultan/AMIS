Below are the code examples for the generator scripts that will help automate the creation of models, views, forms, serializers, and PySide UI files for each module in the medical information system.

### 1. `generate_model.py`

This script generates Django model files for the specified module.

```python
import os

model_template = """from django.db import models

class {ModelName}(models.Model):
    # Add your model fields here
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
"""

def generate_model(module_name, model_name):
    directory = f'../backend/medical_system/models/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, f'{module_name}.py'), 'w') as file:
        file.write(model_template.format(ModelName=model_name))

if __name__ == "__main__":
    module_name = input("Enter the module name: ")
    model_name = input("Enter the model name: ")
    generate_model(module_name, model_name)
    print(f"{model_name} model generated successfully in {module_name}.py")
```

### 2. `generate_view.py`

This script generates Django view files for the specified module.

```python
import os

view_template = """from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import {ModelName}
from .forms import {ModelName}Form

def {module_name}_list(request):
    items = {ModelName}.objects.all()
    return render(request, '{module_name}/{module_name}_list.html', {{ 'items': items }})

def {module_name}_detail(request, pk):
    item = get_object_or_404({ModelName}, pk=pk)
    return render(request, '{module_name}/{module_name}_detail.html', {{ 'item': item }})

def {module_name}_create(request):
    if request.method == 'POST':
        form = {ModelName}Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('{module_name}_list'))
    else:
        form = {ModelName}Form()
    return render(request, '{module_name}/{module_name}_form.html', {{ 'form': form }})

def {module_name}_update(request, pk):
    item = get_object_or_404({ModelName}, pk=pk)
    if request.method == 'POST':
        form = {ModelName}Form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('{module_name}_detail', args=[pk]))
    else:
        form = {ModelName}Form(instance=item)
    return render(request, '{module_name}/{module_name}_form.html', {{ 'form': form }})

def {module_name}_delete(request, pk):
    item = get_object_or_404({ModelName}, pk=pk)
    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect(reverse('{module_name}_list'))
    return render(request, '{module_name}/{module_name}_confirm_delete.html', {{ 'item': item }})
"""

def generate_view(module_name, model_name):
    directory = f'../backend/medical_system/views/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, f'{module_name}_views.py'), 'w') as file:
        file.write(view_template.format(module_name=module_name, ModelName=model_name))

if __name__ == "__main__":
    module_name = input("Enter the module name: ")
    model_name = input("Enter the model name: ")
    generate_view(module_name, model_name)
    print(f"Views for {model_name} generated successfully in {module_name}_views.py")
```

### 3. `generate_form.py`

This script generates Django form files for the specified module.

```python
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
```

### 4. `generate_serializer.py`

This script generates Django serializer files for the specified module.

```python
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
```

### 5. `generate_pyside_ui.py`

This script generates PySide UI files for the specified module.

```python
import os

pyside_ui_template = """from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListView, QLineEdit, QTextEdit, QLabel, QFormLayout

class {ModelName}UI(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.form_layout.addRow("Name", self.name_input)
        self.form_layout.addRow("Description", self.description_input)

        self.layout.addLayout(self.form_layout)

        self.save_button = QPushButton("Save")
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

        self.save_button.clicked.connect(self.save_{module_name})

    def save_{module_name}(self):
        # Implement save functionality here
        pass

    def load_{module_name}(self, data):
        # Implement load functionality here
        pass
"""

def generate_pyside_ui(module_name, model_name):
    directory = f'../frontend/ui/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, f'{module_name}_ui.py'), 'w') as file:
        file.write(pyside_ui_template.format(module_name=module_name, ModelName=model_name))

if __name__ == "__main__":
    module_name = input("Enter the module name: ")
    model_name = input("Enter the model name: ")
    generate_pyside_ui(module_name, model_name)
    print(f"PySide UI for {model_name} generated successfully in {module_name}_ui.py")
```

These scripts will help you quickly generate the necessary files for each module in your medical information system, reducing the amount of manual coding required.
