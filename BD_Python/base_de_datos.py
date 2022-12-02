import mysql.connector
from mysql.connector import Error
#Método init se ejecutara cuando mande a llamar la clase BD
class BD():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(host = 'localhost',
                user = 'root',
                #si no pide contrasña (como XAMPP) se puede quitar la passwd
                #passwd = 'root',
                db = 'peliculas')
        except Error as ex:
            print('La conexion ha tenido un error: ', ex)

    def select(self, tabla):
        if self.conexion.is_connected():
            try:
                script = 'select * from ' + tabla
                cursor = self.conexion.cursor()
                cursor.execute(script)
                consulta = cursor.fetchall()
                return consulta
            except Error as ex:
                print('La conexion ha tenido un error: ', ex)

    def eliminar(self, sentencia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(sentencia)
                #self.conexion.commit
            except Error as ex:
                print('La conexion ha tenido un error: ', ex)

bd = BD()