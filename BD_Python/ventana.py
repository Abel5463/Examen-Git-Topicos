#Para lo de SQL de la plataforma buscar todos los drops y en los constraint de los drops agregar esto al final:
#on delete cascade on update cascade
#F3 para buscar palabras 


from tkinter import *
from tkinter import ttk
import base_de_datos

#Agregar algo estético

mysql = base_de_datos.BD()

ventana = Tk()
ventana.title('Mysql con tkinter')
ventana.geometry('600x500')

#Variables, StringVar() Nos permite compartir variables entre tkinter y python
#Id','Pelicula','Genero','Duración','Nombre director'
pelicula = StringVar()
genero = StringVar()
duracion = StringVar()
nombre_director = StringVar()

#Agregamos LableFrame
marco = LabelFrame(ventana, text = 'Tabla personas')
#tkinter toma como referencia el eje superior izquierdo para acomodar la pantalla
marco.place(x=50,y=50,width=500,height=400)
#Agregamos Label y textinput para nombre, correo y telefono
#El grid es como una cuadricula
lblPelicula = Label(marco,text='Pelicula: ', fg= 'green')
lblPelicula.grid(column=1, row=0, padx=5, pady=5)
txtPelicula = Entry(marco, textvariable=pelicula)
txtPelicula.grid(column=1, row=1)

lblGenero = Label(marco,text='Genero: ', fg= 'green')
lblGenero.grid(column=1, row=2, padx=5, pady=5)
txtGenero = Entry(marco, textvariable=genero)
txtGenero.grid(column=1, row=3)

lblDuracion = Label(marco,text='Duración: ', fg= 'green')
lblDuracion.grid(column=1, row=4, padx=5, pady=5)
txtDuracion = Entry(marco, textvariable=duracion)
txtDuracion.grid(column=1, row=5)

lblDuracion = Label(marco,text='Nombre director: ', fg= 'green')
lblDuracion.grid(column=1, row=4, padx=5, pady=5)
txtDuracion = Entry(marco, textvariable=nombre_director)
txtDuracion.grid(column=1, row=5)



#Le pasamos que se va a almacenar en marco
#Arbol de vistas (buscar imagen en google para saber que es un arbol de vistas)
tvPeliculas = ttk.Treeview(marco)
tvPeliculas.grid(column=3, row=0, columnspan=5)
tvPeliculas['columns'] = ('Id','Pelicula','Genero','Duración','Nombre director')
#Como la primer columna esta vacía la "eliminamos" o sea, le ponemos ancho de 0 para que no se vea
tvPeliculas.column('#0', width=0, stretch=NO)
tvPeliculas.column('Id', width=100, anchor=CENTER)
tvPeliculas.column('Pelicula', width=100, anchor=CENTER)
tvPeliculas.column('Genero', width=100, anchor=CENTER)
tvPeliculas.column('Duración', width=100, anchor=CENTER)
tvPeliculas.column('Nombre director', width=100, anchor=CENTER)
tvPeliculas.heading('Id', text='Id',anchor=CENTER)
tvPeliculas.heading('Pelicula', text='Pelicula',anchor=CENTER)
tvPeliculas.heading('Genero', text='Genero',anchor=CENTER)
tvPeliculas.heading('Duración', text='Duración',anchor=CENTER)
tvPeliculas.heading('Nombre director', text='Nombre director',anchor=CENTER)

btnAgregar = Button(marco,text='Agregar',command=lambda:agregar())
btnAgregar.grid(column=0, row=4,pady=5)

btnActualizar = Button(marco,text='Actualizar',command=lambda:llenar_tabla())
btnActualizar.grid(column=1, row=4,pady=5)

btnEliminar = Button(marco,text='Eliminar',command=lambda:eliminar())
btnEliminar.grid(column=2, row=4,pady=5)

def validar():
    return len(nombre.get()) and len(correo.get()) and len(telefono.get())

def limpiar():
    nombre.set('')
    correo.set('')
    telefono.set('')

def vaciar_tabla():
    filas = tvPersonas.get_children()
    for fila in filas:
        tvPersonas.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    consulta = mysql.select('personas')
    for fila in consulta:
        id = fila[0]
        tvPersonas.insert('',END,text=id,values=fila)

def agregar():
    if validar():
        variables = nombre.get(), correo.get(), telefono.get()
        sql = 'insert from personas into (nombre,correo,telefono) values (%s,%s,%s)'
        mysql.agregar(sql)
        llenar_tabla()
        limpiar()
        
def actualizar():
    pass

def eliminar():
    #Esto no es para eliminar pero lo estamos haciendo aquí por algún motivo
    item_seleccionado = tvPersonas.focus()
    detalle = tvPersonas.item(item_seleccionado)
    id = detalle.get('values')[0]
    #print(id)
    if id > 0:
        sql = 'delete from personas where id = ' + str(id)
        mysql.eliminar(sql)
        llenar_tabla()

llenar_tabla()
ventana.mainloop()

