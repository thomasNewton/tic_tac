from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'X'
        self.setGeometry(100, 100, 760, 800)
        self.setFixedSize(760, 800)
        self.gridLayout = QGridLayout()  # Create a grid layout with 3 rows and 3 columns
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(5)
        self.setLayout(self.gridLayout)
        for row in range(3):  # Create 9 buttons and add them to the grid layout
            for col in range(3):
                button = QPushButton()
                button.setFixedSize(240, 240)
                button.setStyleSheet("background-color: rgb(170, 200, 240)")
                button.clicked.connect(lambda row=row, col=col: self.button_clicked(row, col))
                self.gridLayout.addWidget(button, row, col)
        self.turnLabel = QLabel(f"Turn: {self.turn}")  # Create a label to display the current turn
        self.turnLabel.setAlignment(Qt.AlignCenter)
        self.turnLabel.setFixedSize(220, 50)
        self.turnLabel.setStyleSheet("background-color: rgb(228,225,245); color: rgb(12,7,43); font-size: 40px")
        self.gridLayout.addWidget(self.turnLabel, 3, 0, 1, 3)
        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedSize(220, 50)
        self.reset_button.setStyleSheet("background-color: rgb(228,225,245); color: darkRed; font-size: 40px")
        self.reset_button.clicked.connect(self.reset_game)
        self.gridLayout.addWidget(self.reset_button, 3, 1, 1, 2)
        self.win_label = QLabel(f"Ready")
        self.win_label.setAlignment(Qt.AlignCenter)
        self.win_label.setFixedSize(220, 50)
        self.win_label.setStyleSheet("background-color: rgb(228,225,245); color: rgb(12,7,43); font-size: 40px;"
                                    "font: bold italic large")
        'Times New Roman'
        self.gridLayout.addWidget(self.win_label, 3, 2, 1, 3)

    def button_clicked(self, row, col):
        # This function will be called when any button is clicked
        # check to see if it is a valid move = ''
        if self.board[row][col] == '':
            self.update_button(row, col)
            self.update_board(row, col)
            self.win_label.setText("Playing...")
            for i in range(3):  # print the board to console to verify  -- can take out
                print(self.board[i])
            print("")
            if not self.check_winner():
                self.update_turn()
                if self.check_tie():
                    print("Tie Game")
                    self.win_label.setText("Tie Game")
                    self.turnLabel.setText(f"No Winner")
            else:  # deal with a winner
                print(f"chicken dinner for {self.turn}")
                self.win_label.setText("Game Over")
                self.turnLabel.setText(f"{self.turn} Won!")




    def update_button(self, row, col):
        # Update the text of the button at (row, col) to the current turn
        # .widget() gets the object at that location
        button = self.gridLayout.itemAtPosition(row, col).widget()
        if self.turn == "X":
            button.setStyleSheet("background-color: rgb(174, 232, 208); color: rgb(36,4,69);"
                                 " font-size: 180px;font: bold italic large 'Times New Roman'")
        else:
            button.setStyleSheet("background-color: rgb(232, 200, 175); color: rgb(4, 41, 8);"
                                 " font-size: 190px;font: bold italic large 'Times New Roman'  ")
        button.setText(f"{self.turn}")

    def update_board(self, row, col):
        self.board[row][col] = self.turn

    def check_winner(self):  # check the game board for winning conditions or a tie
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def update_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        self.turnLabel.setText(f"Turn {self.turn}")

    def reset_game(self): # resets the game to the original start state
        print("Reset the game")
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'X'
        self.turnLabel.setText(f"Turn {self.turn}")
        self.win_label.setText("Ready")
        for row in range(3):
            for col in range(3):
                button = self.gridLayout.itemAtPosition(row, col).widget()
                button.setStyleSheet("background-color: rgb(170, 200, 240)")
                button.setText(None)

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None or self.board[i][j] == '':
                    return False
        return True


if __name__ == "__main__":
    # Create the application and the main window   all boilerplate pyside6 stuff
    app = QApplication([])  # main pyside object  but--- not the gui window
    window = MainWindow()  # - the custom class defined above
    window.show()  # Show the window and run the application
    app.exec()  # runs the main application loop for the pyside main object
