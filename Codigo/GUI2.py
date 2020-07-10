import tkinter as tk
from tkinter import ttk
import funciones

root = tk.Tk()
root.title("Aoe II optimizador v 1.0")
fuente = ['font1', 'font2', 'font3', 'font4']
style = ttk.Style()
style.configure("BW.TLabel", justify='LEFT')


# --------------Start Code Here  'Variables'---------------------------------

tec_mad = tk.StringVar(root, value='aem')
tec_oro = tk.StringVar(root, value='aem')
tec_pie = tk.StringVar(root, value='aem')
mejora_economica = tk.StringVar(root, value='sin_mej')
troop = tk.StringVar(root, value='Sin Seleccionar')
cant_unidades = tk.IntVar(root, value=1)
edad_actual = tk.StringVar(root, value='aem')

# --------------End Code Here-----------------------------------------------


# --------------Start Code Here  'Column 1'-------------------------------------

x0y0 = ttk.Label(root, text="-------------------Tecnologias------------", style="BW.TLabel")
x0y0.grid(column=0, row=0)
x0y1 = ttk.Label(root, text=" ------Madera---- ", style="BW.TLabel")
x0y1.grid(column=0, row=1)
x0y2 = ttk.Radiobutton(root, text=" Sin tecnologia ", variable=tec_mad, value='aem')
x0y2.grid(column=0, row=2, sticky='W')
x0y3 = ttk.Radiobutton(root, text=" Hacha de doble filo ", variable=tec_mad, value='feu')
x0y3.grid(column=0, row=3, sticky='W')
x0y4 = ttk.Radiobutton(root, text=" Sierra de arco ", variable=tec_mad, value='cast')
x0y4.grid(column=0, row=4, sticky='W')
x0y5 = ttk.Radiobutton(root, text=" Sierra a dos ", variable=tec_mad, value='imp')
x0y5.grid(column=0, row=5, sticky='W')
x0y6 = ttk.Label(root, text=" ----Oro---- ", style="BW.TLabel")
x0y6.grid(column=0, row=6)
x0y7 = ttk.Radiobutton(root, text=" Sin tecnologia ", variable=tec_oro, value='aem')
x0y7.grid(column=0, row=7, sticky='W')
x0y8 = ttk.Radiobutton(root, text=" Mineria Aurifera ", variable=tec_oro, value='feu')
x0y8.grid(column=0, row=8, sticky='W')
x0y9 = ttk.Radiobutton(root, text=" Pozo Minero Aurifero ", variable=tec_oro, value='cast')
x0y9.grid(column=0, row=9, sticky='W')
x0y10 = ttk.Label(root, text=" ----Piedra---- ", style="BW.TLabel")
x0y10.grid(column=0, row=10)
x0y11 = ttk.Radiobutton(root, text=" Sin tecnologia ", variable=tec_pie, value='aem')
x0y11.grid(column=0, row=11, sticky='W')
x0y12 = ttk.Radiobutton(root, text=" Explotacion de canteras ", variable=tec_pie, value='feu')
x0y12.grid(column=0, row=12, sticky='W')
x0y13 = ttk.Radiobutton(root, text=" Pozo de canteras ", variable=tec_pie, value='cast')
x0y13.grid(column=0, row=13, sticky='W')

# --------------Mejoras Civs-----------------------------------------------

x1y0 = ttk.Label(root, text="-------------Mejora de Civilizacion---------", style="BW.TLabel")
x1y0.grid(column=1, row=0)
x1y1 = ttk.Radiobutton(root, text=" Sin mejora ", variable=mejora_economica, value='sin_mej')
x1y1.grid(column=1, row=1, sticky='W')
x1y2 = ttk.Radiobutton(root, text=" Aztecas ", variable=mejora_economica, value='aztecas')
x1y2.grid(column=1, row=2, sticky='W')
x1y3 = ttk.Radiobutton(root, text=" Bereberes", variable=mejora_economica, value='bereberes')
x1y3.grid(column=1, row=3, sticky='W')
x1y4 = ttk.Radiobutton(root, text=" Bizantinos ", variable=mejora_economica, value='bizantinos')
x1y4.grid(column=1, row=4, sticky='W')
x1y5 = ttk.Radiobutton(root, text=" Celtas ", variable=mejora_economica, value='celtas')
x1y5.grid(column=1, row=5, sticky='W')
x1y6 = ttk.Radiobutton(root, text=" Coreanos ", variable=mejora_economica, value='coreanos')
x1y6.grid(column=1, row=6, sticky='W')
x1y7 = ttk.Radiobutton(root, text=" Eslavos ", variable=mejora_economica, value='eslavos')
x1y7.grid(column=1, row=7, sticky='W')
x1y8 = ttk.Radiobutton(root, text=" Francos ", variable=mejora_economica, value='francos')
x1y8.grid(column=1, row=8, sticky='W')
x1y9 = ttk.Radiobutton(root, text=" Godos ", variable=mejora_economica, value='godos')
x1y9.grid(column=1, row=9, sticky='W')
x1y10 = ttk.Radiobutton(root, text=" Hunos ", variable=mejora_economica, value='hunos')
x1y10.grid(column=1, row=10, sticky='W')
x1y11 = ttk.Radiobutton(root, text=" Ingleses ", variable=mejora_economica, value='ingleses')
x1y11.grid(column=1, row=11, sticky='W')
x1y12 = ttk.Radiobutton(root, text=" Malayos ", variable=mejora_economica, value='malayos')
x1y12.grid(column=1, row=12, sticky='W')
x1y13 = ttk.Radiobutton(root, text=" Mayas ", variable=mejora_economica, value='mayas')
x1y13.grid(column=1, row=13, sticky='W')
x1y14 = ttk.Radiobutton(root, text=" Mongoles ", variable=mejora_economica, value='mongoles')
x1y14.grid(column=1, row=14, sticky='W')
x1y15 = ttk.Radiobutton(root, text=" Portugueses ", variable=mejora_economica, value='portugueses')
x1y15.grid(column=1, row=15, sticky='W')
x1y16 = ttk.Radiobutton(root, text=" Turcos ", variable=mejora_economica, value='turcos')
x1y16.grid(column=1, row=16, sticky='W')

# -------------- Tropas ---------------------------------------------------------

x2y0 = ttk.Label(text="-------------Tropas-------------", style="BW.TLabel")
x2y0.grid(column=2, row=0)
x2y1 = ttk.Label(text="----Cuartel----", style="BW.TLabel")
x2y1.grid(column=2, row=1)
x2y2 = ttk.Menubutton(text='Linea de milicia')
x2y2.grid(column=2, row=2, sticky='W')

x2y2.menu = tk.Menu(root)
x2y2["menu"] = x2y2.menu

x2y2.menu.add_radiobutton(label="Milicia", variable=troop, value='milicia')
x2y2.menu.add_radiobutton(label="Hombre de armas", variable=troop, value='hda')
x2y2.menu.add_radiobutton(label="Espadachin de espada larga", variable=troop, value='eel')
x2y2.menu.add_radiobutton(label="Espadachin de mandoble", variable=troop, value='em')
x2y2.menu.add_radiobutton(label="Campeon", variable=troop, value='camp')

x2y3 = ttk.Menubutton(text='Linea de lancero')
x2y3.grid(column=2, row=3, sticky='W')

x2y3.menu = tk.Menu(root)
x2y3["menu"] = x2y3.menu

x2y3.menu.add_radiobutton(label="Lancero", variable=troop, value='lanc')
x2y3.menu.add_radiobutton(label="Piquero", variable=troop, value='piq')
x2y3.menu.add_radiobutton(label="Alabardero", variable=troop, value='ala')

x2y4 = ttk.Menubutton(text='Linea de Aguilas')
x2y4.grid(column=2, row=4, sticky='W')

x2y4.menu = tk.Menu(root)
x2y4["menu"] = x2y4.menu

x2y4.menu.add_radiobutton(label="Explorador Aguila", variable=troop, value='expagui')
x2y4.menu.add_radiobutton(label="Guerrero Aguila", variable=troop, value='gueragui')
x2y4.menu.add_radiobutton(label="Guerrero Aguila de Elite", variable=troop, value='gueraguiel')

x2y5 = ttk.Label(text="----Arqueria----", style="BW.TLabel")
x2y5.grid(column=2, row=5)
x2y6 = ttk.Menubutton(text='Linea de arqueros')
x2y6.grid(column=2, row=6, sticky='W')

x2y6.menu = tk.Menu(root)
x2y6["menu"] = x2y6.menu

x2y6.menu.add_radiobutton(label="Arquero", variable=troop, value='arquero')
x2y6.menu.add_radiobutton(label="Ballestero", variable=troop, value='ballestero')
x2y6.menu.add_radiobutton(label="Ballesta", variable=troop, value='ballesta')

x2y7 = ttk.Menubutton(text='Linea de guerrilleros')
x2y7.grid(column=2, row=7, sticky='W')

x2y7.menu = tk.Menu(root)
x2y7["menu"] = x2y7.menu

x2y7.menu.add_radiobutton(label="Guerrillero", variable=troop, value='guerrillero')
x2y7.menu.add_radiobutton(label="Guerrillero de Elite", variable=troop, value='guerrilleroe')
x2y7.menu.add_radiobutton(label="Guerrillero de Elite Imperial", variable=troop, value='guerrilleroeimp')

x2y8 = ttk.Menubutton(text='Linea de arquero a caballo')
x2y8.grid(column=2, row=8, sticky='W')

x2y8.menu = tk.Menu(root)
x2y8["menu"] = x2y8.menu

x2y8.menu.add_radiobutton(label="Arquero a caballo", variable=troop, value='arqueroc')
x2y8.menu.add_radiobutton(label="Arquero a caballo pesado", variable=troop, value='arquerocp')

x2y9 = ttk.Menubutton(text='Linea de artilleria')
x2y9.grid(column=2, row=9, sticky='W')

x2y9.menu = tk.Menu(root)
x2y9["menu"] = x2y9.menu

x2y9.menu.add_radiobutton(label="Artillero Manual", variable=troop, value='artillero')

x2y10 = ttk.Label(text="----Establo----", style="BW.TLabel")
x2y10.grid(column=2, row=10)
x2y11 = ttk.Menubutton(text='Linea de explorador')
x2y11.grid(column=2, row=11, sticky='W')

x2y11.menu = tk.Menu(root)
x2y11["menu"] = x2y11.menu

x2y11.menu.add_radiobutton(label="Explorador", variable=troop, value='explorador')
x2y11.menu.add_radiobutton(label="Caballeria ligera", variable=troop, value='caballeria ligera')
x2y11.menu.add_radiobutton(label="Husar", variable=troop, value='husar')

x2y12 = ttk.Menubutton(text='Linea de Jinete')
x2y12.grid(column=2, row=12, sticky='W')

x2y12.menu = tk.Menu(root)
x2y12["menu"] = x2y12.menu

x2y12.menu.add_radiobutton(label="Jinete", variable=troop, value='jinete')
x2y12.menu.add_radiobutton(label="Caballero", variable=troop, value='caballero')
x2y12.menu.add_radiobutton(label="Paladin", variable=troop, value='paladin')

x2y13 = ttk.Menubutton(text='Linea de Camello')
x2y13.grid(column=2, row=13, sticky='W')

x2y13.menu = tk.Menu(root)
x2y13["menu"] = x2y13.menu

x2y13.menu.add_radiobutton(label="Camello", variable=troop, value='camello')
x2y13.menu.add_radiobutton(label="Camello Pesado", variable=troop, value='camellop')

x2y14 = ttk.Menubutton(text='Linea de Elefantes')
x2y14.grid(column=2, row=14, sticky='W')

x2y14.menu = tk.Menu(root)
x2y14["menu"] = x2y14.menu

x2y14.menu.add_radiobutton(label="Elefante de Combate", variable=troop, value='elefcom')
x2y14.menu.add_radiobutton(label="Elefante de Combate de Elite", variable=troop, value='elefcomelit')


# ------- Edad Actual --------------------------------------------------------------------------------------------------

x3y0 = ttk.Label(root, text='--------Edad Actual-------------')
x3y0.grid(column=3, row=0, sticky='w')

x3y1 = ttk.Radiobutton(root, variable=edad_actual, value='aem', text='Alta edad media')
x3y1.grid(column=3, row=1, sticky='w')

x3y2 = ttk.Radiobutton(root, variable=edad_actual, value='feu', text='Edad Feudal')
x3y2.grid(column=3, row=2, sticky='w')

x3y3 = ttk.Radiobutton(root, variable=edad_actual, value='cas', text='Edad de los Castillos')
x3y3.grid(column=3, row=3, sticky='w')

x3y4 = ttk.Radiobutton(root, variable=edad_actual, value='imp', text='Edad Imperial')
x3y4.grid(column=3, row=4, sticky='w')


# Parte Inferior ---------------------------------------------------------------------------------------


calcular_recursos = ttk.Button(root, text='Calcular Recursos', state=tk.NORMAL,
                               command=lambda: show(True))
calcular_recursos.grid(row=14, column=0)
can = ttk.Label(root, text="Cantidad de unidades")
can.grid(column=0, row=15)
unt = ttk.Entry(root, textvariable=cant_unidades)
unt.grid(column=0, row=16)
can = ttk.Label(root, text="         ")
can.grid(column=0, row=17)
can = ttk.Label(root, text="         ")
can.grid(column=0, row=18)

autor = ttk.Label(root, text= 'by Volk')
autor.grid(column=4, row=20)


# --------------End Code Here-----------------------------------------------


def show(value):
    mad = tec_mad.get()
    oro = tec_oro.get()
    pie = tec_pie.get()
    mej = mejora_economica.get()
    tro = troop.get()
    canti = cant_unidades.get()
    edad = edad_actual.get()

    recursos = funciones.aldeanos_necesarios(tro, [mad, oro, pie], mej, canti, edad)

    mader = 'Madera: ' + str(recursos[0])
    alime = 'Alimento: ' + str(recursos[1])
    orooo = 'Oro: ' + str(recursos[2])

    uni = 'Unidad: ' + funciones.nombre_unidad(troop.get())
    un = uni.ljust(50)
    uni = ttk.Label(root, text=un, background='white')
    uni.grid(column=0, row=17, sticky='W')
    sup = ttk.Label(root, text='Aldeanos necesarios')
    sup.grid(column=0, row=18)
    made = ttk.Label(root, text=mader)
    made.grid(column=0, row=19)
    ali = ttk.Label(root, text=alime)
    ali.grid(column=0, row=20)
    oroo = ttk.Label(root, text=orooo)
    oroo.grid(column=0, row=21)

# --------------End Code Here-----------------------------------------------


root.mainloop()

# End File
