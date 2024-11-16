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
