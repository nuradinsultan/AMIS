from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from database import add_patient, add_appointment, get_departments

class ReceptionistApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Receptionist Dashboard")
        self.setGeometry(100, 100, 500, 500)

        # Layouts
        layout = QVBoxLayout()

        # Patient Registration Form
        self.form_layout = QFormLayout()

        # Inputs for patient data
        self.identifier_input = QLineEdit()
        self.family_name_input = QLineEdit()
        self.given_name_input = QLineEdit()
        self.gender_input = QLineEdit()
        self.birth_date_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()

        self.form_layout.addRow("Identifier:", self.identifier_input)
        self.form_layout.addRow("Family Name:", self.family_name_input)
        self.form_layout.addRow("Given Name:", self.given_name_input)
        self.form_layout.addRow("Gender:", self.gender_input)
        self.form_layout.addRow("Birth Date (YYYY-MM-DD):", self.birth_date_input)
        self.form_layout.addRow("Phone:", self.phone_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("Address:", self.address_input)

        # Dropdown for department
        self.department_dropdown = QComboBox()
        for dept_id, dept_name in get_departments():
            self.department_dropdown.addItem(dept_name, dept_id)
        self.form_layout.addRow("Assign Department:", self.department_dropdown)

        # Appointment inputs
        self.doctor_input = QLineEdit()
        self.appointment_date_input = QLineEdit()
        self.form_layout.addRow("Doctor:", self.doctor_input)
        self.form_layout.addRow("Appointment Date (YYYY-MM-DD):", self.appointment_date_input)

        # Register Button
        self.register_button = QPushButton("Register and Schedule Appointment")
        self.register_button.clicked.connect(self.register_patient_and_schedule)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def register_patient_and_schedule(self):
        patient_data = {
            "id": self.identifier_input.text(),
            "family_name": self.family_name_input.text(),
            "given_name": self.given_name_input.text(),
            "gender": self.gender_input.text(),
            "birth_date": self.birth_date_input.text(),
            "phone": self.phone_input.text(),
            "email": self.email_input.text(),
            "address": self.address_input.text(),
        }

        appointment_data = {
            "patient_id": self.identifier_input.text(),
            "department_id": self.department_dropdown.currentData(),
            "doctor_name": self.doctor_input.text(),
            "appointment_date": self.appointment_date_input.text(),
        }

        add_patient(patient_data)
        add_appointment(appointment_data)
        QMessageBox.information(self, "Success", "Patient registered and appointment scheduled.")
