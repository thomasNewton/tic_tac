from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Button Example")
        self.setGeometry(100, 100, 300, 200)

        # Create the button and add it to the window
        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(100, 50, 100, 50)

        # Add a listener to the button that prints a message to the console
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())