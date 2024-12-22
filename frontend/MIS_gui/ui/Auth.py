from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from receptionist import ReceptionistApp
from admin import AdminApp
import sqlite3

DB_NAME = "healthcare.db"

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        # Layouts
        layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        # Username and Password
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.form_layout.addRow("Username:", self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter Password")
        self.form_layout.addRow("Password:", self.password_input)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.authenticate_user)

        layout.addLayout(self.form_layout)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def authenticate_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            role = user[0]
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}! Role: {role}")
            self.open_application(role)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid Username or Password")

    def open_application(self, role):
        if role == "Receptionist":
            self.receptionist_app = ReceptionistApp()
            self.receptionist_app.show()
        elif role == "Admin":
            self.admin_app = AdminApp()
            self.admin_app.show()
        self.close()
