# Librerías
from PyQt6 import QtWidgets, uic
import sqlite3

#inicar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
principal = uic.loadUi("principal.ui")
login = uic.loadUi("login.ui")

def gui_login():
    login.show()

#Validación de usuario y contraseña con base de datos sqlite3
def validacion_login():
    # Conexión a la base de datos
    conexion = sqlite3.connect("login.db")
    cursor = conexion.cursor()
    # Consulta a la base de datos
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (login.usuario_IS.text(), login.contraseña_IS.text()))
    # Recuperar los resultados de la consulta
    if cursor.fetchall():
        gui_login_correcto()
    else:
        gui_login_incorrecto()
    # Cerrar la conexión
    conexion.close()



def gui_login_correcto():
    login.show()
    principal.hide()


def gui_login_incorrecto():
    login.show()


#botones
principal.botonInicioSesion.clicked.connect(gui_login)
login.botonIngresar_IS.clicked.connect(gui_login_correcto)
#login.botonIngresar_IS.clicked.connect(gui_login_correcto)


#ejecutable
principal.show()
app.exec()





