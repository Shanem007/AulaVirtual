from PyQt6 import QtWidgets, uic

#inicar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
inicio = uic.loadUi("inicio.ui")
login = uic.loadUi("login.ui")
login_correcto = uic.loadUi("login_correcto.ui")
login_incorrecto = uic.loadUi("login_incorrecto.ui")

#ejecutable
inicio.show()
app.exec()




