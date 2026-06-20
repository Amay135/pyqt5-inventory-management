import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from login import Ui_Form as Ui_LoginForm
from daftar import Ui_Form as Ui_RegisterForm
from mainlayout import Ui_Form as Ui_MainLayout

# Simple in-memory database to store users
users_db = {}

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        
        self.ui.pushButtonMasuk.clicked.connect(self.handle_login)
        self.ui.pushButtonMendaftar.clicked.connect(self.open_register)
        self.ui.pushButtonBatal.clicked.connect(self.close)

    def handle_login(self):
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit.text()

        if username in users_db and users_db[username] == password:
            self.main_layout = MainLayoutWindow()
            self.main_layout.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Username or Password is incorrect")

    def open_register(self):
        self.register = RegisterWindow()
        self.register.show()
        self.close()

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        
        self.ui.pushButtonDaftar.clicked.connect(self.handle_register)
        self.ui.pushButton.clicked.connect(self.back_to_login)

    def handle_register(self):
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit.text()

        if username in users_db:
            QMessageBox.warning(self, "Error", "Username already exists")
        else:
            users_db[username] = password
            QMessageBox.information(self, "Success", "Registration successful")
            self.back_to_login()

    def back_to_login(self):
        self.login = LoginWindow()
        self.login.show()
        self.close()

class MainLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainLayout()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.pushButtonSimpan.clicked.connect(self.add_item)
        self.ui.pushButtonHapus.clicked.connect(self.delete_item)

    def add_item(self):
        # Get the values from the input fields
        nama_barang = self.ui.lineEdit.text()
        banyak_barang = self.ui.lineEdit_2.text()
        harga_barang = self.ui.lineEdit_3.text()

        if not nama_barang or not banyak_barang or not harga_barang:
            QMessageBox.warning(self, "Error", "All fields must be filled")
            return

        # Add the values to the table
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(nama_barang))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(banyak_barang))
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(harga_barang))

        # Clear the input fields after adding the item
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def delete_item(self):
        # Get the currently selected row
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            # Remove the selected row
            self.ui.tableWidget.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Error", "No item selected to delete")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
