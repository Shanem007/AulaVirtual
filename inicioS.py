# Librerías
from PyQt6 import QtWidgets, uic 
import sqlite3


#inicar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
principal = uic.loadUi("principal.ui")
login = uic.loadUi("login.ui")
login_correcto = uic.loadUi("login_correcto.ui")
login_error = uic.loadUi("login_error.ui")
registro = uic.loadUi("registro.ui")
base = uic.loadUi("base.ui")

def gui_login():
    login.show()
    principal.hide()

#Validación de usuario y contraseña con base de datos sqlite3
"""def validacion_login():
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
    conexion.close()"""

def agregar_usuario():
    # Recuperar los valores de los campos
    Nombre = registro.Nombre.toPlainText()
    Apellido = registro.Apellido.toPlainText()
    NombreUsuario = registro.NombreUsuario.toPlainText()
    CorreoInstitucional = registro.CorreoInstitucional.toPlainText()
    Clave = registro.Clave.text()
    VerificarClave = registro.VerificarClave.text()

    # Conexión a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    # Insertar los datos en la tabla
    cursor.execute("INSERT INTO RegistroDocente (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave, VerificarClave) VALUES (?, ?, ?, ?, ?,?)", (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave,VerificarClave))
    # Guardar los cambios
    conexion.commit()
   # Mostrar la ventana base
    gui_base()
    # Cerrar la conexión
    conexion.close()



def gui_login_correcto():
    login.hide()
    login_correcto.show()


def gui_login_error():
    login.hide()
    login_error.show()

def gui_registro():
    registro.show()
    principal.hide()

def gui_principal():
    principal.show()
    registro.hide()
    base.hide()

def gui_rloginprincipal():
    login.hide()
    principal.show()

def gui_base():
    base.show()



#botones
principal.botonInicioSesion.clicked.connect(gui_login)
#login.botonIngresar_IS.clicked.connect(validacion_login)
login_error.botonRegresar.clicked.connect(gui_login)
principal.botonRegistro.clicked.connect(gui_registro)
registro.botonRegresar1.clicked.connect(gui_principal)
login.botonRegresar_IS.clicked.connect(gui_rloginprincipal)
registro.botonRegistrarse.clicked.connect(agregar_usuario)
base.botonEntendido.clicked.connect(gui_principal)



#ejecutable
principal.show()
app.exec()





