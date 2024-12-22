import sys
import json
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox

class PatientRegistrationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Registration")
        self.setGeometry(100, 100, 400, 400)

        # Layouts
        layout = QVBoxLayout()

        # Patient Registration Form
        self.form_layout = QFormLayout()
        
        # Patient identifier (e.g., patient ID)
        self.identifier_input = QLineEdit()
        self.identifier_input.setPlaceholderText("Enter Patient Identifier")
        self.form_layout.addRow("Identifier:", self.identifier_input)

        # Patient Family Name
        self.family_name_input = QLineEdit()
        self.family_name_input.setPlaceholderText("Enter Family Name")
        self.form_layout.addRow("Family Name:", self.family_name_input)

        # Patient Given Name
        self.given_name_input = QLineEdit()
        self.given_name_input.setPlaceholderText("Enter Given Name")
        self.form_layout.addRow("Given Name:", self.given_name_input)

        # Gender
        self.gender_input = QLineEdit()
        self.gender_input.setPlaceholderText("Enter Gender (Male/Female/Other)")
        self.form_layout.addRow("Gender:", self.gender_input)

        # Birth Date
        self.birth_date_input = QLineEdit()
        self.birth_date_input.setPlaceholderText("Enter Birth Date (YYYY-MM-DD)")
        self.form_layout.addRow("Birth Date:", self.birth_date_input)

        # Phone Number
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter Phone Number")
        self.form_layout.addRow("Phone Number:", self.phone_input)

        # Email Address
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email Address")
        self.form_layout.addRow("Email Address:", self.email_input)

        # Address
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter Address")
        self.form_layout.addRow("Address:", self.address_input)

        # Register Button
        self.register_button = QPushButton("Register Patient")
        self.register_button.clicked.connect(self.register_patient)
        layout.addLayout(self.form_layout)
        layout.addWidget(self.register_button)

        # Patient FHIR Data Display
        self.fhir_data_display = QLabel("FHIR Patient Resource will be shown here.")
        layout.addWidget(self.fhir_data_display)

        self.setLayout(layout)

    def is_valid_date(self, date_str):
        """ Validate the date format as YYYY-MM-DD """
        return bool(re.match(r'\d{4}-\d{2}-\d{2}', date_str))

    def is_valid_email(self, email_str):
        """ Validate email format """
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_str))

    def is_valid_phone(self, phone_str):
        """ Validate phone number format """
        return bool(re.match(r'^\+?\d{10,15}$', phone_str))

    def register_patient(self):
        # Validate required fields
        if not self.identifier_input.text() or not self.family_name_input.text() or not self.given_name_input.text():
            QMessageBox.warning(self, "Input Error", "Identifier, Family Name, and Given Name are required fields.")
            return

        # Validate date format
        if not self.is_valid_date(self.birth_date_input.text()):
            QMessageBox.warning(self, "Input Error", "Invalid Birth Date format. Use YYYY-MM-DD.")
            return

        # Validate email
        if self.email_input.text() and not self.is_valid_email(self.email_input.text()):
            QMessageBox.warning(self, "Input Error", "Invalid Email format.")
            return

        # Validate phone number
        if self.phone_input.text() and not self.is_valid_phone(self.phone_input.text()):
            QMessageBox.warning(self, "Input Error", "Invalid Phone number format.")
            return

        # Prepare patient data
        patient_data = {
            "resourceType": "Patient",
            "id": self.identifier_input.text(),
            "identifier": [{"use": "official", "system": "http://hospital.example.org/patients", "value": self.identifier_input.text()}],
            "name": [{"use": "official", "family": self.family_name_input.text(), "given": [self.given_name_input.text()]}],
            "gender": self.gender_input.text(),
            "birthDate": self.birth_date_input.text(),
            "telecom": [
                {"system": "phone", "value": self.phone_input.text(), "use": "mobile"},
                {"system": "email", "value": self.email_input.text(), "use": "home"}
            ],
            "address": [{"use": "home", "line": [self.address_input.text()], "city": "Unknown", "state": "Unknown", "postalCode": "0000", "country": "Unknown"}],
        }

        # Convert patient data to JSON
        fhir_patient_json = json.dumps(patient_data, indent=4)

        # Display the FHIR resource
        self.fhir_data_display.setText(fhir_patient_json)
        QMessageBox.information(self, "Success", "Patient Registered Successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PatientRegistrationApp()
    window.show()

    sys.exit(app.exec())
