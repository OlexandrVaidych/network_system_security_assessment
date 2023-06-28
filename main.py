import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

from security_assessment import SecurityAssessment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)

        self.visualize_button = QPushButton("Visualize input data", self)
        self.visualize_button.setGeometry(50, 25, 150, 30)
        self.visualize_button.clicked.connect(self.visualize_input_data)

        self.terms_label = QLabel("Terms: T2, T2, T4, T3, T1, T1", self)
        self.terms_label.setGeometry(50, 75, 200, 30)

        self.weight_coeffs_label = QLabel("Weight coefficients: 8, 7, 9, 8, 6, 5", self)
        self.weight_coeffs_label.setGeometry(50, 100, 200, 30)

        self.assess_button = QPushButton("Assess security", self)
        self.assess_button.setGeometry(50, 140, 175, 30)
        self.assess_button.clicked.connect(self.assess_security)

    def visualize_input_data(self):
        criteria = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']
        values = [0.8, 0.7, 0.9, 0.8, 0.6, 0.5]

        # Create a bar chart
        plt.bar(criteria, values)

        # Add label and title
        plt.xlabel("Risks")
        plt.title("Visualization input data")

        plt.show()

    def assess_security(self):
        values = [0.8, 0.7, 0.9, 0.8, 0.6, 0.5]
        weight_coeffs = [8, 7, 9, 8, 6, 5]
        terms = ["T2", "T2", "T4", "T3", "T1", "T1"]

        security_assessment = SecurityAssessment()
        security_assessment.assess_security(values, weight_coeffs, terms)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()