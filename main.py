from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("меню")

vidpochutu_btn = QPushButton("відпочити")
spinbox_sbx = QSpinBox ()
quest_lbl = QLabel("2+2")
varl1_bnt = QRadioButton("1")
varl2_bnt = QRadioButton("2")
varl3_bnt = QRadioButton("3")
varl4_bnt = QRadioButton("4")
answer_btn = QPushButton("відповісти")
group = QGroupBox ("варіант відповідей")


main_line = QVBoxLayout()

horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStretch(1)
horizontal_line1.addWidget(vidpochutu_btn)
horizontal_line1.addWidget(spinbox_sbx)
main_line.addLayout(horizontal_line1)
main_line.addWidget((quest_lbl))


group_main_line = QVBoxLayout()
group_main_line.addWidget(varl1_bnt)
group_main_line.addWidget(varl2_bnt)
group_main_line.addWidget(varl3_bnt)
group_main_line.addWidget(varl4_bnt)
group.setLayout((group_main_line))
main_line.addWidget(group)
main_line.addWidget(answer_btn)


window.setLayout((main_line))
window.show()
app.exec()
