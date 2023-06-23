import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        terms = 0.8, 0.7, 0.9, 0.8, 0.6, 0.5

        self.setGeometry(100, 100, 300, 200)

        self.visualize_button = QPushButton("Visualize input data", self)
        self.visualize_button.setGeometry(50, 25, 150, 30)
        self.visualize_button.clicked.connect(self.visualize_input_data)

        self.terms_label = QLabel("Terms: 0.8, 0.7, 0.9, 0.8, 0.6, 0.5", self)
        self.terms_label.setGeometry(50, 75, 200, 30)

    def visualize_input_data(self):
        criteria = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']
        values = [0.8, 0.7, 0.9, 0.8, 0.6, 0.5]

        # Create a bar chart
        plt.bar(criteria, values)

        # Add label and title
        plt.xlabel("Risks")
        plt.title("Visualization input data")

        plt.show()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()