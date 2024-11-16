from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from ui.inventory_ui import InventoryItemUI
from ui.financial_ui import FinancialUI
from ui.patient_registration_ui import PatientRegistrationUI
from ui.appointment_ui import AppointmentSchedulingUI
# Import other modules' UIs as needed

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to switch between different module UIs
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Add your module UIs to the stacked widget
        self.inventory_ui = InventoryItemUI()  # Inventory module UI
        self.financial_ui = FinancialUI()      # Financial module UI
        self.patient_registration_ui = PatientRegistrationUI()  # Patient Registration UI
        self.appointment_ui = AppointmentSchedulingUI()  # Appointment Scheduling UI

        self.stacked_widget.addWidget(self.inventory_ui)
        self.stacked_widget.addWidget(self.financial_ui)
        self.stacked_widget.addWidget(self.patient_registration_ui)
        self.stacked_widget.addWidget(self.appointment_ui)

        # Set the first UI as the default
        self.stacked_widget.setCurrentWidget(self.inventory_ui)

        # Set window properties
        self.setWindowTitle("Medical Information System")
        self.setGeometry(100, 100, 800, 600)

        # Optional: Implement navigation logic, buttons to switch between modules

        # Example: Adding navigation buttons (if needed)
        # self.nav_bar = QToolBar(self)
        # self.addToolBar(self.nav_bar)
        # self.nav_bar.addAction("Inventory", self.show_inventory_ui)
        # self.nav_bar.addAction("Financial", self.show_financial_ui)

    def show_inventory_ui(self):
        self.stacked_widget.setCurrentWidget(self.inventory_ui)

    def show_financial_ui(self):
        self.stacked_widget.setCurrentWidget(self.financial_ui)

    def show_patient_registration_ui(self):
        self.stacked_widget.setCurrentWidget(self.patient_registration_ui)

    def show_appointment_ui(self):
        self.stacked_widget.setCurrentWidget(self.appointment_ui)


if __name__ == "__main__":
    # Initialize the PySide application
    app = QApplication(sys.argv)

    # Create the main window and display it
    window = MainWindow()
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
