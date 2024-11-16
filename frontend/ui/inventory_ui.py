from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFormLayout, QListView, QTableWidget, QTableWidgetItem
from PySide2.QtCore import Qt
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class InventoryItemUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.quantity_input = QLineEdit()
        self.form_layout.addRow("Name", self.name_input)
        self.form_layout.addRow("Description", self.description_input)
        self.form_layout.addRow("Quantity", self.quantity_input)

        self.layout.addLayout(self.form_layout)

        self.save_button = QPushButton("Save Item")
        self.layout.addWidget(self.save_button)
        
        # Table to display items
        self.items_table = QTableWidget()
        self.layout.addWidget(self.items_table)

        self.setLayout(self.layout)

        # Connect signals to slots
        self.save_button.clicked.connect(self.save_inventory_item)
        self.load_inventory_items()

    def save_inventory_item(self):
        """Save a new inventory item via an API call to the backend."""
        url = os.getenv("API_URL") + "/inventory/"
        data = {
            "name": self.name_input.text(),
            "description": self.description_input.toPlainText(),
            "quantity": self.quantity_input.text(),
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            print("Item saved successfully")
            self.load_inventory_items()
        else:
            print("Failed to save item")

    def load_inventory_items(self):
        """Load inventory items from the backend API and display them in the table."""
        url = os.getenv("API_URL") + "/inventory/"
        response = requests.get(url)
        
        if response.status_code == 200:
            items = response.json()
            self.items_table.setRowCount(len(items))
            self.items_table.setColumnCount(3)  # Name, Description, Quantity
            self.items_table.setHorizontalHeaderLabels(["Name", "Description", "Quantity"])

            for row, item in enumerate(items):
                self.items_table.setItem(row, 0, QTableWidgetItem(item["name"]))
                self.items_table.setItem(row, 1, QTableWidgetItem(item["description"]))
                self.items_table.setItem(row, 2, QTableWidgetItem(str(item["quantity"])))

        else:
            print("Failed to load inventory items")
