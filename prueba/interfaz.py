
from tkinter import *
from tkinter import ttk,filedialog
from tkinter.font import families

root = Tk()
root.title("Robot")

contenedor = Frame(root)
contenedor.pack()
# --------------------------------------------------
lblusuario = Label(contenedor,text='Usuario:',font=("Arial Black",12),justify="right")
lblusuario.grid(row=0,column=0)

txtusuario = Entry(contenedor)
txtusuario.grid(row=0,column=1)


lblclave = Label(contenedor,text='Clave:',font=("Arial Black",12),justify="right")
lblclave.grid(row=0,column=2)

txtclave = Entry(contenedor)
txtclave.grid(row=0,column=3)

#---------------------PARTE CENTRAL-------------------------------
lbltitulo = Label(contenedor,text='Titulo:',font=("Arial Black",12),justify="right")
lbltitulo.grid(row=1,column=0)
txttitulo = Entry(contenedor)
txttitulo.grid(row=1,column=1)

#----------------------------------------------------
lblresumen = Label(contenedor,text='Resúmen:',font=("Arial Black",12),justify="right")
lblresumen.grid(row=2,column=0)
txtresumen = Entry(contenedor)
txtresumen.grid(row=2,column=1)

#----------------------------------------------------
lblcontenido = Label(contenedor,text='Contenido:',font=("Arial Black",12),justify="right")
lblcontenido.grid(row=3,column=0)
txtcontenido = Entry(contenedor)
txtcontenido.grid(row=3,column=1)


#----------------------------------------------------
lblimagen = Label(contenedor,text='Agregar Imagen:',font=("Arial Black",12),justify="right")
lblimagen.grid(row=4,column=0)
txtimagen = com
txtimagen.grid(row=4,column=1)

#----------------------------------------------------
lbltextoalternativo_img = Label(contenedor,text='Texto Alternativo:',font=("Arial Black",12),justify="right")
lbltextoalternativo_img.grid(row=5,column=0)
txttextoalternativo_img = Entry(contenedor)
txttextoalternativo_img.grid(row=5,column=1)

#----------------------------------------------------
lblcategoria = Label(contenedor,text='categoria',font=("Arial Black",12),justify="right")
lblcategoria.grid(row=6,column=0)
txtcategoria = ttk.Combobox(values=[
                                    'Cultura (0)',
                                    'Economía (0)',
                                    'Politica (0)',
                                    'musica,folclor (3)',
                                    'Actividades (13)',
                                    'Editorial (14)',
                                    'Sondeos (0)',
                                    'Actualidad (15)',
                                    'Deportes (0)',
                                    'Hechos (1)',
                                    'Sucesos (2)',
                                    'Panorama (3)',
                                    'Cauca (16)',
                                    'Personajes (0)',
                                    'Sectores (1)',
                                    'Cultura (2)',
                                    'Ciencia (17)',
                                    'Informe central (19)',
                                    'Salud (20)',
                                    'Cocina (0)',
                                    'Belleza (1)',
                                    'Tendencias (2)',
                                    'Tecnología (21)',]).place(x=165,y=180)
# txtcategoria.grid(row=5,column=1)

#----------------------------------------------------
lblvideo = Label(contenedor,text='URL del Video',font=("Arial Black",12),justify="right")
lblvideo.grid(row=7,column=0)
txtvideo = Entry(contenedor)
txtvideo.grid(row=7,column=1)

#----------------------------------------------------
botoninicio = Button(contenedor,text='Iniciar',font=("Arial Black",12),justify="right")
botoninicio.grid(row=8,column=0)











root.mainloop()



