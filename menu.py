from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QVBoxLayout, QApplication)



def show_menu():
    global window_menu
    window_menu = QWidget()
    window_menu.setWindowTitle('Створення нового питання')

    v_line = QVBoxLayout()

    question = QLineEdit()
    right_answer = QLineEdit()
    wrong_answer1 = QLineEdit()
    wrong_answer2 = QLineEdit()
    wrong_answer3 = QLineEdit()

    btn_save = QPushButton('Зберегти питання')

    v_line.addWidget(question)
    v_line.addWidget(right_answer)
    v_line.addWidget(wrong_answer1)
    v_line.addWidget(wrong_answer2)
    v_line.addWidget(wrong_answer3)
    v_line.addWidget(btn_save)

    window_menu.setLayout(v_line)

    window_menu.show()