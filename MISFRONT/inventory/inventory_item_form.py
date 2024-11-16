# frontend/inventory/inventory_item_form.py

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel, QMessageBox
import requests

class InventoryItemForm(QDialog):
    def __init__(self, parent=None, item_id=None):
        super().__init__(parent)
        self.item_id = item_id
        self.setWindowTitle("Inventory Item Form")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)

        self.quantity_label = QLabel("Quantity:")
        self.quantity_spinbox = QSpinBox()
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_spinbox)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_inventory_item)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        if self.item_id:
            self.load_inventory_item()

    def load_inventory_item(self):
        response = requests.get(f'http://localhost:8000/inventory/{self.item_id}/')
        if response.status_code == 200:
            item = response.json()
            self.name_edit.setText(item['name'])
            self.quantity_spinbox.setValue(item['quantity'])

    def save_inventory_item(self):
        data = {
            'name': self.name_edit.text(),
            'quantity': self.quantity_spinbox.value()
        }
        if self.item_id:
            response = requests.put(f'http://localhost:8000/inventory/{self.item_id}/', json=data)
        else:
            response = requests.post('http://localhost:8000/inventory/', json=data)

        if response.status_code in (200, 201):
            QMessageBox.information(self, "Success", "Inventory item saved successfully")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Failed to save inventory item")
