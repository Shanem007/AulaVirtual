from PyQt6 import QtWidgets, uic

#inicar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
principal = uic.loadUi("principal.ui")
login = uic.loadUi("login.ui")

def gui_login():
    login.show()

def gui_login_correcto():
    login.show()

#def gui_login_incorrecto():
 #   login.show()


#botones
principal.botonInicioSesion.clicked.connect(gui_login)
login.botonIngresar_IS.clicked.connect(gui_login_correcto)
#login.botonIngresar_IS.clicked.connect(gui_login_correcto)


#ejecutable
principal.show()
app.exec()





