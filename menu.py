from PyQt6.QtWidgets import *

import database


def menu():
    window = QDialog()
    main_line = QVBoxLayout()

    add_btn = QPushButton("Добавити")
    quest_lbl = QLabel("Запитання")
    quest_ledt = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)

    right_lbl = QLabel("Правильна відповідь")
    right_ledt = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget( right_lbl)
    h2.addWidget( right_ledt)
    main_line.addLayout(h2)

    wrong1_lbl = QLabel("Не правильна відповідь")
    wrong1_ledt = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget( wrong1_lbl)
    h3.addWidget( wrong1_ledt)
    main_line.addLayout(h3)


    wrong2_lbl = QLabel("не правильна відповідь")
    wrong2_ledt = QLineEdit()

    h4 = QHBoxLayout()
    h4.addWidget( wrong2_lbl)
    h4.addWidget( wrong2_ledt)
    main_line.addLayout(h4)

    wrong3_lbl = QLabel("не правильна відповідь")
    wrong3_ledt = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget( wrong3_lbl)
    h5.addWidget( wrong3_ledt)
    main_line.addLayout(h5)

    def add_func():
        new_quest =  {
        "запитання": quest_ledt.text(),
        "Правильна відповідь": right_ledt.text(),
        "Не правильна відповідь1": wrong1_ledt.text(),
        "Не правильна відповідь2": wrong2_ledt.text(),
        "Не правильна відповідь3": wrong3_ledt.text(),

        }
        database.question.append(new_quest)

    add_btn.clicked.connect(add_func)
    main_line.addWidget(add_btn)


    window.setLayout(main_line)
    window.exec()











