import datos_recursos
import datos_tropas


def nombre_unidad(value):

    tropas = {'Sin Seleccionar':    'Sin Seleccionar',
              'milicia':            'Milicia',
              'hda':                'Hombre de Armas',
              'eel':                'Espadachin de Espada Larga',
              'em':                 'Espadachin de Mandoble',
              'camp':               'Campeon',
              'lanc':               'Lancero',
              'piq':                'Piquero',
              'ala':                'Alabardero',
              'expagui':            'Explorador Aguila',
              'gueragui':           'Guerrerro Aguila',
              'gueraguiel':         'Guerro Aguila de Elite',
              'arquero':            'Arquero',
              'ballestero':         'Ballestero',
              'ballesta':           'Ballesta',
              'guerrillero':        'Guerrillero',
              'guerrilleroe':       'Guerrillero de Elite',
              'guerrilleroeimp':    'Guerrillero de Elite Imperial',
              'arqueroc':           'Arquero a Caballo',
              'arquerocp':          'Arquero a Caballo Pesado',
              'artillero':          'Artillero Manual',
              'explorador':         'Explorador',
              'caballeria ligera':  'Caballeria Ligera',
              'husar':              'Husar',
              'jinete':             'Jinete',
              'caballero':          'Caballero',
              'paladin':            'Paladin',
              'camello':            'Camello',
              'camellop':           'Camello con Armadura',
              'camelloimpe':        'Camello Imperial',
              'elefcom':            'Elefante de Combate',
              'elefcomelit':        'Elefante de Combate de Elite',
              }

    ret = tropas[value]

    return ret


def aldeanos_necesarios(unidad, tecnologia, civ, cantidad, edad):

    unid = nombre_unidad(unidad)
    prod = datos_recursos.produccion_x_seg(tecnologia, civ)
    prod = [prod[0], prod[3], prod[1], prod[2]]
    trop = datos_tropas.unidades(unid)
    tiempo_prod = trop[4]

    if (civ == 'turcos') and (unid == 'Artillero Manual'):
        tiempo_prod = tiempo_prod / 1.2

    if (civ == 'bizantinos') and (unid in ['Lancero', 'Piquero', 'Alabardero', 'Guerrillero',
                                           'Guerrillero de Elite', 'Guerrillero de Elite Imperial',
                                           'Camello', 'Camello con Armadura', 'Camello Imperial']):
        time = trop[4]
        trop = [round(trop[i]/1.25, 3) for i in range(4)]
        trop.append(time)

    god_units = ['Hombre de Armas','Espadachin de Espada Larga', 'Espadachin de Mandoble',
                 'Campeon', 'Lancero', 'Piquero', 'Alabardero']

    if (civ == 'godos') and (edad in ['feu', 'cast', 'imp']) and (unid in god_units):
        time = trop[4]
        trop = [round(trop[i]/1.35, 3) for i in range(4)]
        trop.append(time)

    if civ == 'coreanos':
        trop[0] = round(trop[0]/1.15, 3)

    uni_hun = ['Arquero a Caballo', 'Arquero a Caballo Pesado']
    if (civ == 'hunos') and (edad == 'cas') and (unid in uni_hun):
        time = trop[4]
        trop = [round(trop[i]/1.10, 3) for i in range(4)]
        trop.append(time)

    if (civ == 'hunos') and (edad == 'imp') and (unid in uni_hun):
        time = trop[4]
        trop = [round(trop[i]/1.20, 3) for i in range(4)]
        trop.append(time)

    uni_may = ['Arquero', 'Ballestero', 'Ballesta']
    if (civ == 'mayas') and (edad == 'feu') and (unid in uni_may):
        time = trop[4]
        trop = [round(trop[i]/1.10, 3) for i in range(4)]
        trop.append(time)
    if (civ == 'mayas') and (edad == 'cas') and (unid in uni_may):
        time = trop[4]
        trop = [round(trop[i]/1.20, 3) for i in range(4)]
        trop.append(time)
    if (civ == 'mayas') and (edad == 'imp') and (unid in uni_may):
        time = trop[4]
        trop = [round(trop[i]/1.30, 3) for i in range(4)]
        trop.append(time)

    uni_bere = ['Explorador', 'Caballeria Ligera', 'Husar', 'Jinete',
                'Caballero', 'Paladin', 'Camello', 'Camello con Armadura']
    if (civ == 'bereberes') and (edad == 'cas') and (unid in uni_bere):
        time = trop[4]
        trop = [round(trop[i]/1.15, 3) for i in range(4)]
        trop.append(time)
    if (civ == 'bereberes') and (edad == 'imp') and (unid in uni_bere):
        time = trop[4]
        trop = [round(trop[i]/1.20, 3) for i in range(4)]
        trop.append(time)

    if civ == 'portugueses':
        trop[2] = round(trop[2]/1.15, 3)

    uni_malay = ['Elefante de Combate', 'Elefante de Combate de Elite']
    if (civ == 'malayos') and (unid in uni_malay):
        time = trop[4]
        trop = [round(trop[i]/1.30, 3) for i in range(4)]
        trop.append(time)

    prod_unit_norm = [round(trop[i]/tiempo_prod, 3) for i in range(len(trop))]
    prod_unit_norm.pop()
    cant_tropas_producidas = [round(prod_unit_norm[i] * cantidad, 3) for i in range(len(trop)-1)]
    ald_nec = [round(cant_tropas_producidas[i] / prod[i], 1) for i in range(len(prod_unit_norm))]
    ret = ald_nec
    return ret


def civ_w_mej_tiempo(civ):

    civs = ['aztecas', 'celtas', 'godos', 'hunos', 'ingleses', 'turcos']

    if civ in civs:
        ret = civ
    else:
        ret = 'sin_mej'

    return ret


def mejora_de_tiempo(civ):

    civilizacion = civ_w_mej_tiempo(civ)

    bff = {'aztecas':   [1.15, 1.15, 1.15, 1.15, 1.15],
           'celtas':   [1, 1, 1, 1.2, 1],
           'godos':    [1.2, 1, 1, 1, 1],
           'hunos':    [1, 1, 1.2, 1, 1],
           'ingleses': [1, 1.2, 1, 1, 1],
           'sin_mej':  [1, 1, 1, 1, 1]}

    valor = bff[civilizacion]

    return valor


# End code
