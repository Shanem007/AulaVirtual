# Librerías
from PyQt6 import QtWidgets, uic
import sqlite3

#inicar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
principal = uic.loadUi("principal.ui")
login = uic.loadUi("login.ui")
login_correcto = uic.loadUi("login_correcto")
login_error = uic.loadUi("login_error")

def gui_login():
    login.show()

#Validación de usuario y contraseña con base de datos sqlite3
def validacion_login():
    # Conexión a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    # Consulta a la base de datos
    usuario = login.usuario_IS.toPlainText()  # Accede al contenido del widget de usuario
    contraseña = login.clave_IS.toPlainText()  # Accede al contenido del widget de contraseña
    cursor.execute("SELECT * FROM credenciales WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
    # Recuperar los resultados de la consulta
    if cursor.fetchall():
        gui_login_correcto()
    else:
        gui_login_error()
    # Cerrar la conexión
    conexion.close()



def gui_login_correcto():
    login.hide()
    login_correcto.show()


def gui_login_error():
    login.hide()
    login_error.show()


#botones
principal.botonInicioSesion.clicked.connect(gui_login)
login.botonIngresar_IS.clicked.connect(validacion_login)



#ejecutable
principal.show()
app.exec()





