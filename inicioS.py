# Librerías
from PyQt6 import QtWidgets, uic 
import sqlite3
from PyQt6.QtWidgets import QFileDialog  #libreria para subir archivos 
from PyQt6.QtCore import QUrl    #libreria para ver archivos
from PyQt6.QtGui import QDesktopServices #libreria para ver archivos



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
CursoAsignatura1 = uic.loadUi("CursoAsignatura1.ui")
bienvenidaEstudiante = uic.loadUi("bienvenidaEstudiante.ui")
contenido = uic.loadUi("contenido.ui")
Pestañas = uic.loadUi("Pestañas.ui") 

CursosEst = uic.loadUi("CursosEst.ui")     
mtricMate = uic.loadUi("mtricMate.ui")
mtricLengua = uic.loadUi("mtricLengua.ui")
mtricHisto = uic.loadUi("mtricHisto.ui")
mensajeArchivo =uic.loadUi("mensajeArchivo.ui")
ventanaVisualizacionArchivo = uic.loadUi("ventanaVisualizacionArchivo.ui")
Evaluacion = uic.loadUi("Evaluacion.ui")
ventanaPreguntasAbiertas = uic.loadUi("ventanaPreguntasAbiertas.ui")
ventanaPreguntasVF = uic.loadUi("ventanaPreguntasVF.ui")
contenidoCargado = uic.loadUi("contenidoCargado.ui")
ventanaPreguntasAbiertas2 = uic.loadUi("ventanaPreguntasAbiertas2.ui")
ventanaPreguntasVF2 = uic.loadUi("ventanaPreguntasVF2.ui")
ventanaPreguntasOM = uic.loadUi("ventanaPreguntasOM.ui")
preguntas = uic.loadUi("preguntas.ui")
examenRecopilado = uic.loadUi("examenRecopilado.ui")
informeEstu = uic.loadUi("informeEstu.ui")



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
    Clave = registro.Clave.text()   #.text -->cuando usamos un line edit en pyqt6
    VerificarClave = registro.VerificarClave.text()
    


    if Clave != VerificarClave:                              # muestra un aviso que las contraseñas no coinciden 
        registro.Aviso.setText("La contraseña no coincide")  # .setText--> cuando usamos un label
    else:

        # Conexión a la base de datos
        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()
        if registro.rbuttonDocente.isChecked():   #isChecked --> cuando usamos un raddiobutton en pyqt6
             # Insertar los datos en la tabla docente
            cursor.execute("INSERT INTO RegistroDocente (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave, VerificarClave) VALUES (?, ?, ?, ?, ?,?)", (Nombre, Apellido, NombreUsuario, CorreoInstitucional, Clave,VerificarClave))
       
        else:
            registro.rbuttonEstudiante.isChecked() #isChecked --> cuando usamos un raddiobutton en pyqt6
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
    Clave = login.clave_IS.text()  # Accede al contenido del widget de contraseña
    
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
    login.hide() #.hide sirve para ocultar una ventana
    login_correcto.show()  #.show sirve para mostrar una ventana 

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
    CursoAsignatura1.hide()

def gui_CursoAsignatura():
    CursoAsignatura1.show()
    Menu.hide()
            
def gui_bienvenidaEstudiante():
    bienvenidaEstudiante.show()

def gui_contenido():
    contenido.show()

def gui_Pestañas():
    Pestañas.show()



def gui_CursosEst():
    CursosEst.show()
    login.hide()
    bienvenidaEstudiante.hide()

def gui_mtricMate():
    mtricMate.show()

def gui_mtricLengua():
    mtricLengua.show()

def gui_mtricHisto():
    mtricHisto.show()

def gui_Evaluacion():
    Evaluacion.show()

def gui_ventanaPreguntasAbiertas():
    ventanaPreguntasAbiertas.show()

def gui_ventanaPreguntasVF():
    ventanaPreguntasVF.show()

def gui_contenidoCargado():
    contenidoCargado.show()

def gui_preguntas():
    preguntas.show()

def gui_ventanaPreguntasAbiertas2():
    ventanaPreguntasAbiertas2.show()

def gui_ventanaPreguntasVF2():
    ventanaPreguntasVF2.show()

def gui_ventanaPreguntasOM():
    ventanaPreguntasOM.show()

def gui_examenRecopilado():
    examenRecopilado.show()
    
    
    
#Tabla informe de estudiantes       
def gui_informeEstu(self):
    informeEstu.show()
    
    """self.verLista.clicked.connect(self.funcion_verLista)
    self.actualizar1.clicked.connect(self.funcion_actualizar1)
    self.eliminar1.clicked.connect(self.funcion_eliminar1)
    self.Regresarcurso.clicked.connect(self.funcion_Regresarcurso)
        
    self.refrescar.clicked.connect(self.funcion_refrescar)
    self.buscar3.clicked.connect(self.funcion_buscar3)
    self.actualizar2.clicked.connect(self.funcion_actualizar2)
    self.buscar1.clicked.connect(self.funcion_buscar1)
    self.eliminar2.clicked.connect(self.funcion_eliminar2)
        
def funcion_verLista(self):
    # Código a ejecutar cuando se hace clic en verLista
    self.statusBar()

def funcion_actualizar1(self):
    self.statusBar()
    
def funcion_eliminar1(self):
    self.statusBar()
    
def funcion_Regresarcurso(self):
    self.statusBar()
        
def funcion_refrescar(self):
    self.statusBar()
        
        
def funcion_buscar3(self):
    self.statusBar()
        
def funcion_actualizar2(self):
    self.statusBar()
        
def funcion_buscar1(self):
    self.statusBar()
        
def funcion_eliminar2(self):
    self.statusBar()""" 
    


#codigo para subir y visualizar los archivos 

#conexion con la base de datos para subir archivos 
def gui_ventanaVisualizacionArchivo():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    # Obtener la lista de nombres de archivos desde la base de datos
    cursor.execute("SELECT nombre_archivo FROM archivos")
    nombres_archivos = cursor.fetchall()

    ventanaVisualizacionArchivo.comboBoxArchivos.clear()  # Limpiar el combobox
    for nombre_archivo in nombres_archivos:
        ventanaVisualizacionArchivo.comboBoxArchivos.addItem(nombre_archivo[0])  # Agregar nombres al combobox

    conexion.close()
    ventanaVisualizacionArchivo.show()

def ver_contenido_archivo_seleccionado():
    nombre_archivo_seleccionado = ventanaVisualizacionArchivo.comboBoxArchivos.currentText()
    mostrar_contenido_archivo(nombre_archivo_seleccionado)

def abrir_archivo():
    nombre_archivo_seleccionado = ventanaVisualizacionArchivo.comboBoxArchivos.currentText()

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    # Obtener la ruta del archivo desde la base de datos
    cursor.execute("SELECT ruta_archivo FROM archivos WHERE nombre_archivo = ?", (nombre_archivo_seleccionado,))
    resultado = cursor.fetchone()
    
    if resultado:
        archivo_path = resultado[0]
        url = QUrl.fromLocalFile(archivo_path)
        QDesktopServices.openUrl(url)           

    conexion.close()
#funcion para subir archivos 
def cargar_archivo():
    archivo, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de texto (*.txt);;Documentos de Word (*.docx);;Archivos PDF (*.pdf);;Todos los archivos (*)")

    if archivo:
        # Obtener solo el nombre del archivo de la ruta completa
        nombre_archivo = archivo.split("/")[-1]

        # Guardar la información del archivo en la base de datos
        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO archivos (nombre_archivo, ruta_archivo, tipo_archivo) VALUES (?, ?, ?)", (nombre_archivo, archivo, "Tipo del archivo"))
        conexion.commit()
        conexion.close()

        mensajeArchivo.show()
#funcion para ver archivo subido 
def mostrar_contenido_archivo(nombre_archivo):
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    # Obtener la ruta del archivo desde la base de datos
    cursor.execute("SELECT ruta_archivo FROM archivos WHERE nombre_archivo = ?", (nombre_archivo,))
    resultado = cursor.fetchone()
    
    if resultado:
        archivo_path = resultado[0]
        with open(archivo_path, 'r') as archivo:
            contenido = archivo.read()
            ventanaVisualizacionArchivo.archivoSubido.setText(contenido)  # Asignar el contenido al widget QTextEdit
            ventanaVisualizacionArchivo.show()

    conexion.close()

# "r" al inicio en el nombre de las funciones indica que es una función para un boton de regresar y su
# estructura es así: r_ventanaOrigen_ventanaDestino.
#Boton regresar en la pantalla de error de ingreso (Oculta el error y muestra el login)
def r_loginIncorrecto_login():
    login_error.hide()
    login.show()

def r_guiContenido_guiCursoAsignatura():
    contenido.hide()
    CursoAsignatura1.show()

def r_Pestañas_CursoAsignatura():
    Pestañas.hide()
    CursoAsignatura1.show()


def r_informeEstu_CursoAsignatura():
    informeEstu.hide()


def r_CursoAsignatura_Menu():
    CursoAsignatura1.hide()

def r_Menu_login():
    Menu.hide()
    login.show()

def r_cursosEst_bienvenidaestudiante():
    CursosEst.hide()
    bienvenidaEstudiante.show()

def r_bienvenidaEstudiantes_principal():
    bienvenidaEstudiante.hide()
    principal.show()

def r_mtricMate_CursosEst():
    mtricMate.hide()

def r_mtricLengua_CursosEst():
    mtricLengua.hide()

def r_mtricHisto_CursosEst():
    mtricHisto.hide()

def r_mensajeArchivo_Pestañas():
    mensajeArchivo.hide()

def r_ventanaVisualizacionArchivo_Menu():
    ventanaVisualizacionArchivo.hide()

def r_Evaluacion_CursoAsignatura():
    Evaluacion.hide()

def r_ventanaPreguntasAbiertas_Evaluacion():
    ventanaPreguntasAbiertas.hide()
    
def r_ventanaPreguntasVF_Evaluacion():
    ventanaPreguntasVF.hide()

def r_pestañas_CursoAsignatura():
    Pestañas.hide()






#examen 

def agregar_pregunta_abierta():
    pregunta_abierta = ventanaPreguntasAbiertas2.textEditPreguntaAbierta.toPlainText()
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    
    # Insertar la pregunta en la tabla del examen
    cursor.execute("INSERT INTO preguntasExamen (tipo, pregunta) VALUES (?, ?)", ("Pregunta Abierta", pregunta_abierta))
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    
    ventanaPreguntasAbiertas2.hide()

def agregar_pregunta_vf():
    pregunta_vf = ventanaPreguntasVF2.textEditPreguntaVF.toPlainText()
    respuesta_correcta = "Verdadero" if ventanaPreguntasVF2.radioButtonVerdadero.isChecked() else "Falso"
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    
    # Insertar la pregunta en la tabla del examen
    cursor.execute("INSERT INTO preguntasExamen (tipo, pregunta, opciones, respuesta_correcta) VALUES (?, ?, ?, ?)", ("Pregunta Cerrada", pregunta_vf, "Verdadero,Falso", respuesta_correcta))
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    
    ventanaPreguntasVF2.hide()

def agregar_pregunta_om():
    pregunta_om = ventanaPreguntasOM.textEditPreguntaOM.toPlainText()
    opciones_texto = ventanaPreguntasOM.textEditOpciones.toPlainText()
    opciones = opciones_texto.split(',')
    respuesta_correcta = ventanaPreguntasOM.comboBoxRespuesta.currentText()
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    
    # Insertar la pregunta en la tabla del examen
    cursor.execute("INSERT INTO preguntasExamen (tipo, pregunta, opciones, respuesta_correcta) VALUES (?, ?, ?, ?)", ("Pregunta de Opción Múltiple", pregunta_om, opciones_texto, respuesta_correcta))
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    
    ventanaPreguntasOM.hide()

def gui_examenRecopilado():
    # Conexión a la base de datos
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    # Recuperar las preguntas de la base de datos (por ejemplo, las preguntas de tipo "Pregunta Abierta")
    cursor.execute("SELECT pregunta FROM preguntasExamen WHERE tipo = 'Pregunta Abierta'")
    preguntas_abiertas = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    # Mostrar las preguntas en la ventana examenRecopilado
    examenRecopilado.label_3.setText("\n".join([pregunta[0] for pregunta in preguntas_abiertas]))
    # Mostrar la ventana examenRecopilado
    examenRecopilado.show()
















#botones
# estructura:ventana.nombre del boton.clicked(al hacer click).connect(se conecta a una funcion) (función a donde se dirige)
principal.botonInicioSesion.clicked.connect(gui_login)
login.botonIngresar_IS.clicked.connect(validacion_login)
login_error.botonRegresar.clicked.connect(r_loginIncorrecto_login) #boton regresar
principal.botonRegistro.clicked.connect(gui_registro)
registro.botonRegresar1.clicked.connect(gui_principal)
login.botonRegresar_IS.clicked.connect(gui_rloginprincipal)
registro.botonRegistrarse.clicked.connect(agregar_usuario)
base.botonEntendido.clicked.connect(gui_principal)
login_correcto.botonEntendido.clicked.connect(gui_Menu)
Menu.botonEditar.clicked.connect(gui_CursoAsignatura)
CursoAsignatura1.botonContenido.clicked.connect(gui_contenido)
CursoAsignatura1.botonDoc.clicked.connect(gui_Pestañas)

contenido.botonCancelar.clicked.connect(r_guiContenido_guiCursoAsignatura)
Pestañas.botonOk.clicked.connect(r_Pestañas_CursoAsignatura) #boton regresar

CursoAsignatura1.botoRegresarCurso.clicked.connect(gui_Menu)
Menu.botonRegresarMenu.clicked.connect(r_Menu_login) #boton regresar
bienvenidaEstudiante.botonIrCurso.clicked.connect(gui_CursosEst)
CursosEst.botonCursoMatematica.clicked.connect(gui_mtricMate)
CursosEst.botonCursoLengua.clicked.connect(gui_mtricLengua)
CursosEst.botonCursoHistoria.clicked.connect(gui_mtricHisto)
CursosEst.botonRegresarCursos.clicked.connect(r_cursosEst_bienvenidaestudiante) #boton regresar
bienvenidaEstudiante.botonSalirBienvenida.clicked.connect(r_bienvenidaEstudiantes_principal) #boton regresar
mtricMate.botonCancelarMate.clicked.connect(r_mtricMate_CursosEst) #boton regresar
mtricLengua.botonCancelarLengua.clicked.connect(r_mtricLengua_CursosEst) #boton regresar
mtricHisto.botonCancelarHisto.clicked.connect(r_mtricHisto_CursosEst)  #boton regresar
Pestañas.botonSubirDoc.clicked.connect(cargar_archivo)
mensajeArchivo.botonEntendidoArchivo.clicked.connect(r_mensajeArchivo_Pestañas)
Menu.botonVer.clicked.connect(gui_ventanaVisualizacionArchivo)
ventanaVisualizacionArchivo.botonAbrirArchivo.clicked.connect(abrir_archivo) #abre los archivos 
ventanaVisualizacionArchivo.botonEntendidoArchivo.clicked.connect(r_ventanaVisualizacionArchivo_Menu)
CursoAsignatura1.botonEvaluacion.clicked.connect(gui_Evaluacion)
Evaluacion.botonAddVF.clicked.connect(gui_ventanaPreguntasVF)
Evaluacion.botonAddA.clicked.connect(gui_ventanaPreguntasAbiertas)
Evaluacion.botonRegresarEval.clicked.connect(r_Evaluacion_CursoAsignatura)
ventanaPreguntasVF.botonRegresarVF.clicked.connect(r_ventanaPreguntasVF_Evaluacion) #boton regresar
ventanaPreguntasAbiertas.botonRegresarA.clicked.connect(r_ventanaPreguntasAbiertas_Evaluacion) #boton regresar
Menu.botoncontenidoCargado.clicked.connect(gui_contenidoCargado)
Pestañas.botonRegresarPes.clicked.connect(r_pestañas_CursoAsignatura) #boton regresar
Menu.botonPreguntas.clicked.connect(gui_preguntas)
preguntas.botonPreguntasAbiertas.clicked.connect(gui_ventanaPreguntasAbiertas2)
preguntas.botonPreguntasCerradas.clicked.connect(gui_ventanaPreguntasVF2)
preguntas.botonPreguntasOpcionMultiple.clicked.connect(gui_ventanaPreguntasOM)
Menu.botonExamenRecopilado.clicked.connect(gui_examenRecopilado)
CursoAsignatura1.botonInforme.clicked.connect(gui_informeEstu)

# informeEstu.botonRegresarcurso.clicked.connect(r_informeEstu_CursoAsignatura) #boton regresar

#botones de las preguntas 
Evaluacion.botonAddA.clicked.connect(gui_ventanaPreguntasAbiertas2)
ventanaPreguntasAbiertas2.botonAgregarPreguntaAbierta.clicked.connect(agregar_pregunta_abierta)
ventanaPreguntasVF2.botonAgregarPreguntaVF.clicked.connect(agregar_pregunta_vf)  # Agregar pregunta cerrada
ventanaPreguntasOM.botonAgregarPreguntaOM.clicked.connect(agregar_pregunta_om)


#ejecutable
principal.show()
app.exec()

