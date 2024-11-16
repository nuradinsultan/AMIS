# frontend/inventory/inventory_item_list.py

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QListWidget, QWidget, QPushButton, QLabel, QHBoxLayout
import requests

class InventoryItemList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Item List")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.load_inventory_items()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_inventory_items(self):
        response = requests.get('http://localhost:8000/inventory/')
        if response.status_code == 200:
            items = response.json()
            for item in items:
                self.list_widget.addItem(f"{item['name']} (Quantity: {item['quantity']})")

if __name__ == '__main__':
    app = QApplication([])
    window = InventoryItemList()
    window.show()
    app.exec()
