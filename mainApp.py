# import library PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from app_calc import Ui_MainWindow  # import class to use in this code

# variable for deleting input (line-edit) after an making an opertion
check = True

# variable for saving last value (ans button) none he has nothing
var_ans = None

#slots
# butons functions 
def affiche0():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"0")
    else :
        ui.lineEdit.setText("0")
        check = True

# buton 1
def affiche1():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"1")
    else :
        ui.lineEdit.setText("1")
        check = True

# buton 2  
def affiche2():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"2")
    else :
        ui.lineEdit.setText("2")
        check = True

# buton 3   
def affiche3():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"3")
    else :
        ui.lineEdit.setText("3")
        check = True

# buton 4    
def affiche4():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"4")
    else :
        ui.lineEdit.setText("4")
        check = True

# buton 5   
def affiche5():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"5")
    else :
        ui.lineEdit.setText("5")
        check = True

# buton 6    
def affiche6():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"6")
    else :
        ui.lineEdit.setText("6")
        check = True

# buton 7    
def affiche7():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"7")
    else :
        ui.lineEdit.setText("7")
        check = True

# buton 8    
def affiche8():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"8")
    else :
        ui.lineEdit.setText("8")
        check = True

# buton 9   
def affiche9():
    global check
    if check == True :
        ui.lineEdit.setText(ui.lineEdit.text()+"9")
    else :
        ui.lineEdit.setText("9")
        check = True

# buton .  
def affichePoint():
    ui.lineEdit.setText(ui.lineEdit.text()+".")

# buton /
def afficheDivise():
    ui.lineEdit.setText(ui.lineEdit.text()+"/")

# buton *
def afficheMultiply():
    ui.lineEdit.setText(ui.lineEdit.text()+"*")

# buton -
def afficheMinus():
    ui.lineEdit.setText(ui.lineEdit.text()+"-")

# buton + 
def affichePlus():
    ui.lineEdit.setText(ui.lineEdit.text()+"+")

# buton Ac like "clear" we use "" for delete all inside lineedit
def afficheAc():
    ui.lineEdit.setText("")

# buton del [:-1] to delete value before last 
def afficheDelete():
    ui.lineEdit.setText(ui.lineEdit.text()[:-1])

# buton = we use eval() for adding two str and give int ... setText accept str so we transform it   
def afficheEqual():
    global check
    try:
        text = eval(ui.lineEdit.text())
        ui.lineEdit.setText(str(text))
    except ZeroDivisionError:# error of divide by 0 in program
        ui.lineEdit.setText("Cannot divide by zero !")
    except SyntaxError:# other errors of program 
        ui.lineEdit.setText("Invalid operation !")
    
    check = False  # i put false to return value from functions to delete it





import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#connections
# les evenements ou connection lorsqu'on click sur bouton
ui.b_0.clicked.connect(affiche0)
ui.b_1.clicked.connect(affiche1)
ui.b_2.clicked.connect(affiche2)
ui.b_3.clicked.connect(affiche3)
ui.b_4.clicked.connect(affiche4)
ui.b_5.clicked.connect(affiche5)
ui.b_6.clicked.connect(affiche6)
ui.b_7.clicked.connect(affiche7)
ui.b_8.clicked.connect(affiche8)
ui.b_9.clicked.connect(affiche9)
ui.b_point.clicked.connect(affichePoint)
ui.b_divide.clicked.connect(afficheDivise)
ui.b_multiply.clicked.connect(afficheMultiply)
ui.b_minus.clicked.connect(afficheMinus)
ui.b_plus.clicked.connect(affichePlus)
ui.b_ac.clicked.connect(afficheAc)
ui.b_del.clicked.connect(afficheDelete)
ui.b_equal.clicked.connect(afficheEqual)


sys.exit(app.exec_())