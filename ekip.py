import sys 
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow, QMenu,  QComboBox
from PyQt5.uic import loadUi
import pymysql
from datetime import datetime
import sys 
import traceback
import pymysql
import sqlite3

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login = 'Danya'
password = '1111'

class Login(QDialog):
                    
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login.ui",self)

        self.pushButton.clicked.connect(self.glmenu)

    def glmenu(self):
        lg = self.lineEdit_2.text()
        psw = self.lineEdit.text()
        
        if lg == login and psw == password:
            mainwindow = Admin()
            widget.addWidget(mainwindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.about(self, "Ошибка", "Неккоректная авторизация")
            

class Admin(QDialog):
    def pechat(self):
        with open('Отчёт.txt', 'w', encoding='UTF-8') as out_file:
            print("---------------------------------------------------", file=out_file)
            print("| ФИО | Пол | Возраст | Звание | Отряд |  Машина  |", file=out_file)
            print("---------------------------------------------------", file=out_file)
            for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    print('|'+item.text(), end='| ', file=out_file) 
                print('', file=out_file)  
    
    def zapros(self):#функция запроса
        zapr = self.lineEdit_2.text()#переменная введённого условия в запрос
        cmbx = self.comboBox.currentText()#переменная выбранного пункта в комбо бокс 1
        cmbx2 = self.comboBox_2.currentText()#переменная выбранного пункта в комбо бокс 2

        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()

        try:
            if cmbx == 'ФИО':
                cur = con.cursor()
                sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.FIO LIKE '{zapr}%'"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            elif cmbx == 'ВОЗРАСТ':
                cur = con.cursor()
                if cmbx2 == "<":
                    sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.Old < {zapr}"
                if cmbx2 == ">":
                    sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.Old > {zapr}"
                if cmbx2 == "=":
                    sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.Old = {zapr}"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            elif cmbx == 'ПОЛ':
                cur = con.cursor()
                sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.Gender = {zapr}"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            elif cmbx == 'ЗВАНИЕ':
                cur = con.cursor()
                sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE sotrudniki.Zvanie = '{zapr}'"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            elif cmbx == 'ОТРЯД':
                cur = con.cursor()
                sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE otryad.Naznach = '{zapr}'"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            elif cmbx == 'МАШИНА':
                cur = con.cursor()
                sqlquery = f"SELECT sotrudniki.FIO,sotrudniki.Gender,sotrudniki.Old,sotrudniki.Zvanie,otryad.Naznach,transport.NameTr FROM sosttr INNER JOIN otryad ON sosttr.IDOtr = otryad.IDOtr INNER JOIN sotrudniki ON sotrudniki.IDOtr = otryad.IDOtr INNER JOIN transport ON sosttr.IDTr = transport.IDTr WHERE transport.NameTr = '{zapr}'"
                result = cur.execute(sqlquery)
                con.commit()
                itog = cur.fetchall()
                cc = 5
            
            self.tableWidget.clear()

            row = 0
            column = 0

            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(6)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 5:
                        row += 1
                        column = 0
                    else:
                        column += 1

            self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Пол", "Возраст", "Звание", "Отряд", "Машина"])

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")

        
    
    
    def loadbd(self):
        con = sqlite3.connect('GOST.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Clients')
        itog = cur.fetchall()
        con.commit()
        con.close()

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 5:
                    row += 1
                    column = 0
                else:
                    column += 1
    
    def __init__(self):
        super(Admin,self).__init__()
        loadUi("glmenu.ui",self)
        widget.setFixedWidth(600)
        widget.setFixedHeight(477)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()
        
        self.pushButton_5.clicked.connect(self.sotr)
        self.pushButton_2.clicked.connect(self.otr)
        self.pushButton_3.clicked.connect(self.sostotr)
        self.pushButton_4.clicked.connect(self.tran)
        self.pushButton.clicked.connect(self.zapros)
        self.pushButton_6.clicked.connect(self.pechat)
        
        
    def sotr(self):
        sotrr = Sotrudniki()
        widget.addWidget(sotrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def otr(self):
        otrr = Otryad()
        widget.addWidget(otrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def tran(self):
        tranr = Transport()
        widget.addWidget(tranr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def sostotr(self):
        sostotrr = Sostotr()
        widget.addWidget(sostotrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Sotrudniki(QDialog):
    def loadbd(self):
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        sqlquery = "SELECT * from sotrudniki"
        cur = con.cursor()
        result = cur.execute(sqlquery)
        itog = cur.fetchall()

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 5:
                    row += 1
                    column = 0
                else:
                    column += 1

        self.tableWidget.setHorizontalHeaderLabels(["ID", "ФИО", "Пол", "Возраст", "Звание", "ID Отряда"])

    def dobavzp(self):
        ids = self.lineEdit.text()
        fio = self.lineEdit_2.text()
        gen = self.lineEdit_3.text()
        old = self.lineEdit_4.text()
        zv = self.lineEdit_5.text()
        idot = self.lineEdit_6.text()

        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"INSERT INTO sotrudniki VALUES({ids},'{fio}',{gen},{old},'{zv}',{idot})"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")

        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Дублирование данных!")

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пустой ввод данных!")

    def udalzp(self):
        ids = self.lineEdit_7.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"DELETE FROM sotrudniki WHERE ID = {ids}"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")

    def izmzp(self):
        ids = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        if cmbx == 'ФИО':
            izm = 'FIO'
            sqlquery = f"UPDATE sotrudniki SET {izm} = '{upd}' WHERE ID = {ids}"
        elif cmbx == 'Пол':
            izm = 'Gender'
            sqlquery = f"UPDATE sotrudniki SET {izm} = {upd} WHERE ID = {ids}"
        elif cmbx == 'Возраст':
            izm = 'Old'
            sqlquery = f"UPDATE sotrudniki SET {izm} = {upd} WHERE ID = {ids}"
        elif cmbx == 'Звание':
            izm = 'Zvanie'
            sqlquery = f"UPDATE sotrudniki SET {izm} = '{upd}' WHERE ID = {ids}"
        elif cmbx == 'ID Отряда':
            izm = 'IDOtr'
            sqlquery = f"UPDATE sotrudniki SET {izm} = {upd} WHERE ID = {ids}"
        try:
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Несуществующее значение!")
                    
    def __init__(self):
        super(Sotrudniki,self).__init__()
        loadUi("sotrudniki.ui",self)
        widget.setFixedWidth(601)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Transport(QDialog):
    def loadbd(self):
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        sqlquery = "SELECT * from transport"
        cur = con.cursor()
        result = cur.execute(sqlquery)
        itog = cur.fetchall()

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setHorizontalHeaderLabels(["ID Трансп.", "Название"])

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 1:
                    row += 1
                    column = 0
                else:
                    column += 1
    
    def dobavzp(self):
        idtr = self.lineEdit.text()
        name = self.lineEdit_2.text()

        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"INSERT INTO transport VALUES({idtr},'{name}')"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")

        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Дублирование данных!")

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пустой ввод данных!")

    def udalzp(self):
        idtr = self.lineEdit_7.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"DELETE FROM transport WHERE IDTr = {idtr}"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Транспорт привязан к другой таблице!")

    def izmzp(self):
        idtr = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        if cmbx == 'Название':
            izm = 'NameTr'
            sqlquery = f"UPDATE transport SET {izm} = '{upd}' WHERE IDTr = {idtr}"
        try:
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")
    
    def __init__(self):
        super(Transport,self).__init__()
        loadUi("Transport.ui",self)
        widget.setFixedWidth(201)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Sostotr(QDialog):
    def loadbd(self):
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        sqlquery = "SELECT * from sosttr"
        cur = con.cursor()
        result = cur.execute(sqlquery)
        itog = cur.fetchall()

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 1:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Отряда","ID Трансп."])
    
    def dobavzp(self):
        idotr = self.lineEdit.text()
        idtr = self.lineEdit_2.text()

        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"INSERT INTO sosttr VALUES({idtr},{idotr})"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")

        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Дублирование данных или ввод несуществующих значений!")

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пустой ввод данных!")

    def udalzp(self):
        idotr = self.lineEdit_7.text()
        idtr = self.lineEdit_10.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"DELETE FROM sosttr WHERE IDTr = {idtr} and IDOtr = {idotr}"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")
    
    def __init__(self):
        super(Sostotr,self).__init__()
        loadUi("Sostotr.ui",self)
        widget.setFixedWidth(201)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Otryad(QDialog):
    def loadbd(self):
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        sqlquery = "SELECT * from otryad"
        cur = con.cursor()
        result = cur.execute(sqlquery)
        itog = cur.fetchall()

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 1:
                    row += 1
                    column = 0
                else:
                    column += 1

        self.tableWidget.setHorizontalHeaderLabels(["ID Отряда","Назначение"])
    
    def dobavzp(self):
        idotr = self.lineEdit.text()
        name = self.lineEdit_2.text()

        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"INSERT INTO otryad VALUES({idotr},'{name}')"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")

        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Дублирование данных!")

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пустой ввод данных!")

    def udalzp(self):
        idotr = self.lineEdit_7.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        try:
            sqlquery = f"DELETE FROM otryad WHERE IDOtr = {idotr}"
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Отряд привязан к другой таблице!")

    def izmzp(self):
        idotr = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        con = pymysql.connect(
        host = 'localhost',
        database = 'shemetovrg',
        user = 'root',
        passwd = '1111')
        cur = con.cursor()
        if cmbx == 'Назначение':
            izm = 'Naznach'
            sqlquery = f"UPDATE otryad SET {izm} = '{upd}' WHERE IDOTr = {idotr}"
        try:
            result = cur.execute(sqlquery)
            con.commit()
            
            self.tableWidget.clear()
            self.loadbd()

        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")
    
    def __init__(self):
        super(Otryad,self).__init__()
        loadUi("Otryad.ui",self)
        widget.setFixedWidth(201)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


con = pymysql.connect(
                    host = 'localhost',
                    database = 'ShemetovRG',
                    user = 'root',
                    passwd = '1111',
                    charset='utf8')
cur = con.cursor() 
mainwindow = Login()
widget.addWidget(mainwindow)
widget.setFixedWidth(113)
widget.setFixedHeight(63)
widget.show()
widget.setWindowTitle('Шеметов РГ')
app.exec_()
