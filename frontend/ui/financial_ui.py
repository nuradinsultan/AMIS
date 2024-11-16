from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class FinancialUI(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # Table to display financial records
        self.financial_table = QTableWidget()
        self.layout.addWidget(self.financial_table)

        self.refresh_button = QPushButton("Refresh Financial Records")
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)

        # Connect signals
        self.refresh_button.clicked.connect(self.load_financial_records)

        # Initially load records
        self.load_financial_records()

    def load_financial_records(self):
        """Load financial records from the backend API."""
        url = os.getenv("API_URL") + "/financial/"
        response = requests.get(url)

        if response.status_code == 200:
            records = response.json()
            self.financial_table.setRowCount(len(records))
            self.financial_table.setColumnCount(3)  # Example: Date, Amount, Description
            self.financial_table.setHorizontalHeaderLabels(["Date", "Amount", "Description"])

            for row, record in enumerate(records):
                self.financial_table.setItem(row, 0, QTableWidgetItem(record["date"]))
                self.financial_table.setItem(row, 1, QTableWidgetItem(str(record["amount"])))
                self.financial_table.setItem(row, 2, QTableWidgetItem(record["description"]))
        else:
            print("Failed to load financial records")
