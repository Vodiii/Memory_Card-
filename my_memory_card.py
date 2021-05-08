#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QLabel,QHBoxLayout,
QMessageBox,QRadioButton,QGroupBox,QButtonGroup)
from random import shuffle
from random import randint
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственный язык Бразилии?','Португальский','Английский','Испанский',"Бразильский"))
question_list.append(Question('Государственный язык Китая?','Китайский','Английский','Итальянский',"Русский"))
question_list.append(Question('Кто первый полетел в космос?','Гагарин','Леонов','Марашин',"Чин"))
question_list.append(Question('Марка первой машины в мире?','Ford','Hunday','Porshe',"Lada"))
question_list.append(Question('Крупнейшая поисковая система? ','Google','Яндекс','Amazon',"Facebook"))
question_list.append(Question('Минимальное количество герц на мониторе?','60','144','280',"360"))
question_list.append(Question('В каком классе добавляется история?','5','4','7',"6"))
question_list.append(Question('Первый штраф был выписан на скорость(m/ч)?','13','10','6',"22"))
question_list.append(Question('В каком году был выпущен первый телефон?','1973','1966','1982',"1972"))
question_list.append(Question('В каком году был изобретен первый компьютер? ','1927','1922','1963',"1924"))
app = QApplication([])
main_win = QWidget()
layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()
RadioGroupBox = QGroupBox("Варианты ответов:")
lb_question = QLabel('Какой национальности не существует?"')
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чумыльцы")
rbtn_4 = QRadioButton("Алеуты")
ans = QPushButton("Ответить")
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q):
    shuffle(answers)
    lb_question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    y_n_1.setText(q.right_answer)
    show_question()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
main_win.cur_questhion = -1

def next_quethion():
    main_win.total+=1
    cur_questhion = randint(0,len(question_list) - 1)
    
    q = question_list[cur_questhion]
    ask(q)
    print('Всего:',main_win.total)
    print("Правильных ответов",main_win.score)
    
    print('Статистика',main_win.score/main_win.total*100)


answer = QGroupBox("Результаты теста")
y_n = QLabel('Правильно/Неправильно')
y_n_1 = QLabel('Правильный ответ')
layout_ans6 = QVBoxLayout()
layout_ans6.addWidget(y_n)
layout_ans6.addWidget(y_n_1)
answer.setLayout(layout_ans6)

layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()
layout_1.addWidget(lb_question)
layout_2.addWidget(RadioGroupBox)
layout_2.addWidget(answer)
layout_3.addWidget(ans)

layout_otvet = QVBoxLayout()

layout_main = QVBoxLayout()

layout_main.addLayout(layout_1)
layout_main.addLayout(layout_2)
layout_main.addLayout(layout_3)
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
answer.hide()  
def show_correct(res):
    y_n.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        main_win.score+=1
        show_correct('Правильно')
    else:
        if answers[3].isChecked() or answers[1].isChecked() or answers[2].isChecked():
            show_correct('Неправильно!')
            

def show_result():
    RadioGroupBox.hide()
    answer.show()
    ans.setText("Следующий вопрос")
def show_question():
    RadioGroupBox.show()
    answer.hide()
    ans.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def click_OK():

    if ans.text()==("Ответить"):
        check_answer()
    else:
        next_quethion()


ans.clicked.connect(click_OK)
main_win.total = 0
main_win.score = 0
main_win.setLayout(layout_main)
main_win.show()
app.exec_()