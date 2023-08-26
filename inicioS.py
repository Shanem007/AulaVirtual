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
Menu = uic.loadUi("Menu.ui")
CursoAsignatura = uic.loadUi("CursoAsignatura.ui")
bienvenidaEstudiante = uic.loadUi("bienvenidaEstudiante.ui")
contenido = uic.loadUi("contenido.ui")
Pestañas = uic.loadUi("Pestañas.ui") 
informenotas = uic.loadUi("informenotas.ui")      

def gui_login():
    login.show()
    principal.hide()

#base de datos 
def agregar_usuario():
    # Recuperar los valores de los campos
    Nombre = registro.Nombre.toPlainText()
    Apellido = registro.Apellido.toPlainText() #.toPlainText--> cuando usamos un textedit en pyqt6
    NombreUsuario = registro.NombreUsuario.toPlainText()
    CorreoInstitucional = registro.CorreoInstitucional.toPlainText()
    Clave = registro.Clave.text()
    VerificarClave = registro.VerificarClave.text()
    


    if Clave != VerificarClave:
        registro.Aviso.setText("La contraseña no coincide")
    else:

        # Conexión a la base de datos
        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()
        if registro.rbuttonDocente.isChecked():
             # Insertar los datos en la tabla docente
            cursor.execute("INSERT INTO RegistroDocente (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave, VerificarClave) VALUES (?, ?, ?, ?, ?,?)", (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave,VerificarClave))
       
        else:
            registro.rbuttonEstudiante.isChecked() #isChecked -->cuando usamos un raddiobutton en pyqt6
         # Insertar los datos en la tabla estudiante
            cursor.execute("INSERT INTO RegistroEstudiante (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave, VerificarClave) VALUES (?, ?, ?, ?, ?,?)", (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave,VerificarClave))
       
        # Guardar los cambios
        conexion.commit()
        # Mostrar la ventana base
        gui_base()
        # Cerrar la conexión
        conexion.close()

#Validación de usuario y contraseña con base de datos sqlite3
def validacion_login():
    # Conexión a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    # Consulta a la base de datos
    NombreUsuario = login.usuario_IS.toPlainText()  # Accede al contenido del widget de usuario
    Clave = login.clave_IS.toPlainText()  # Accede al contenido del widget de contraseña
    
    if login.rbuttonDocente.isChecked():
        cursor.execute("SELECT * FROM RegistroDocente WHERE NombreUsuario = ? AND Clave = ?", (NombreUsuario, Clave))
    else:
        login.rbuttonEstudiante.isChecked()
        cursor.execute("SELECT * FROM RegistroEstudiante WHERE Nombreusuario = ? AND Clave = ?", (NombreUsuario, Clave))

    # Recuperar los resultados de la consulta
    if cursor.fetchall():
        if login.rbuttonDocente.isChecked():
            gui_login_correcto()  # Mostrar ventana de login correcto
        else:
            gui_bienvenidaEstudiante()  # Mostrar ventana de bienvenida para estudiantes
    else:
        gui_login_error()

    
        # Cerrar la conexión   
        conexion.close()

#GUI indica las funciones de las ventanas

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

def gui_Menu():
    Menu.show()
    login_correcto.hide()

def gui_CursoAsignatura():
    CursoAsignatura.show()
    Menu.hide()

def gui_bienvenidaEstudiante():
    bienvenidaEstudiante.show()

def gui_contenido():
    contenido.show()

def gui_Pestañas():
    Pestañas.show()

def gui_informenotas():
    informenotas.show()

# "r" al inicio en el nombre de las funciones indica que es una función para un boton de regresar y su
# estructura es así: r_ventanaOrigen_ventanaDestino.
#Boton regresar en la pantalla de error de ingreso (Oculta el error y muestra el login)
def r_loginIncorrecto_login():
    login_error.hide()
    login.show()

def r_guiContenido_guiCursoAsignatura():
    contenido.hide()
    CursoAsignatura.show()

#botones
# estructura:ventana.nombre del boton.clicked(al hacer click).connect(se conecta a una funcion) (función a donde se dirige)
principal.botonInicioSesion.clicked.connect(gui_login)
login.botonIngresar_IS.clicked.connect(validacion_login)
login_error.botonRegresar.clicked.connect(r_loginIncorrecto_login)
principal.botonRegistro.clicked.connect(gui_registro)
registro.botonRegresar1.clicked.connect(gui_principal)
login.botonRegresar_IS.clicked.connect(gui_rloginprincipal)
registro.botonRegistrarse.clicked.connect(agregar_usuario)
base.botonEntendido.clicked.connect(gui_principal)
login_correcto.botonEntendido.clicked.connect(gui_Menu)
Menu.botonVer.clicked.connect(gui_CursoAsignatura)
CursoAsignatura.botonContenido.clicked.connect(gui_contenido)
CursoAsignatura.botonDoc.clicked.connect(gui_Pestañas)
CursoAsignatura.botonInforme.clicked.connect(gui_informenotas)
contenido.botonCancelar.clicked.connect(r_guiContenido_guiCursoAsignatura)



#ejecutable
principal.show()
app.exec()





