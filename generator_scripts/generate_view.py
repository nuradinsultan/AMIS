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
