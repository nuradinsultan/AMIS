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

