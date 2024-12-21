import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Management System")
        self.setGeometry(100, 100, 800, 600)

        # Set up main layout
        main_layout = QVBoxLayout()

        # Header label
        header = QLabel("Patient Management System")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # Horizontal navigation bar
        nav_layout = QHBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(QWidget(), "Patient Note")
        tabs.addTab(QWidget(), "Glass Prescription")
        tabs.addTab(QWidget(), "Investigation")
        tabs.addTab(QWidget(), "Consultation")
        tabs.addTab(QWidget(), "Procedure")
        tabs.addTab(QWidget(), "Physiotherapy")
        tabs.addTab(QWidget(), "Medication")
        tabs.addTab(QWidget(), "Vital Signs")
        tabs.addTab(QWidget(), "Assignments")
        tabs.addTab(QWidget(), "Admission")
        tabs.addTab(QWidget(), "Report")
        
        nav_layout.addWidget(tabs)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

