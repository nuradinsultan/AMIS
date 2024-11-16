# frontend/inventory/inventory_dashboard.py

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from .inventory_item_list import InventoryItemList

class InventoryDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list_button = QPushButton("List Inventory Items")
        self.list_button.clicked.connect(self.show_inventory_list)
        layout.addWidget(self.list_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_inventory_list(self):
        self.inventory_list = InventoryItemList()
        self.inventory_list.show()

if __name__ == '__main__':
    app = QApplication([])
    dashboard = InventoryDashboard()
    dashboard.show()
    app.exec()
