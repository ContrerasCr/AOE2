def unidades(value):

    # Sin Seleccionar --------------------------------------------------------------------------------------------------

    ret = [0, 0, 0, 0, 1]
    sin_seleccionar = [0, 0, 0, 0, 1]
    if value == 'Sin Seleccionar':
        ret = sin_seleccionar

    # Alta edad media

    milicia = [0, 60, 20, 0, 21]
    if value == 'Milicia':
        ret = milicia

    # Feudal -----------------------------------------------------------------------------------------------------------

    # unidad = madera,alimento,oro,piedra,tiempo de produccion]

    guerrillero = [25, 35, 0, 0, 22]
    arquero = [25, 0, 45, 0, 35]
    scout = [0, 80, 0, 0, 30]
    lancero = [25, 35, 0, 0, 22]
    hombre_de_armas = [0, 60, 20,  0, 22]
    explorador_aguila = [0, 20, 50, 0, 35]

    if value == 'Guerrillero':
        ret = guerrillero
    if value == 'Arquero':
        ret = arquero
    if value == 'Explorador':
        ret = scout
    if value == 'Lancero':
        ret = lancero
    if value == 'Hombre de Armas':
        ret = hombre_de_armas
    if value == 'Explorador Aguila':
        ret = explorador_aguila

    # Castillos---------------------------------------------------------------------------------------------------------

    # Cuartel

    espada_larga = [0, 60, 20, 0, 22]
    piquero = [25, 35, 0, 0, 22]
    aguila = [0, 20, 50, 0, 35]

    if value == 'Espadachin de Espada Larga':
        ret = espada_larga
    if value == 'Piquero':
        ret = piquero
    if value == 'Guerrero Aguila':
        ret = aguila

    # arqueria

    ballestero = [25, 0, 35, 0, 27]
    guerrillero_elite = [25, 35, 0, 0, 22]
    arquero_a_caballo = [40, 0, 60, 0, 34]

    if value == 'Ballestero':
        ret = ballestero
    if value == 'Guerrillero de Elite':
        ret = guerrillero_elite
    if value == 'Arquero a Caballo':
        ret = arquero_a_caballo

    # Establo

    caballeria_ligera = [25, 35, 0, 0, 30]
    jinete = [0, 60, 75, 0, 30]
    camello = [0, 55, 60, 0, 22]
    elefante = [0, 120, 70, 0, 28]

    if value == 'Caballeria Ligera':
        ret = caballeria_ligera
    if value == 'Jinete':
        ret = jinete
    if value == 'Camello':
        ret = camello
    if value == 'Elefante de Combate':
        ret = elefante

    # Taller de maquinaria

    ariete = [25, 35, 0, 0, 35]
    mangonel = [160, 0, 135, 0, 46]
    escorpion = [75, 0, 75, 0, 30]

    if value == 'Ariete':
        ret = ariete
    if value == 'Mangonel':
        ret = mangonel
    if value == 'Escorpion':
        ret = escorpion

    # Imperial ---------------------------------------------------------------------------------------------------------
    # Cuartel

    espadachin_mandoble = [0, 60, 20, 0, 21]
    campeon = [0, 60, 20, 0, 21]
    alabadero = [25, 35, 0, 0, 22]
    aguila_elite = [0, 20, 50, 0, 35]

    if value == 'Espadachin de Mandoble':
        ret = espadachin_mandoble
    if value == 'Campeon':
        ret = campeon
    if value == 'Alabardero':
        ret = alabadero
    if value == 'Guerrero Aguila de Elite':
        ret = aguila_elite

    # Arqueria

    ballesta = [25, 0, 35, 0, 27]
    guerrillero_elite_imp = [25, 35, 0, 0, 22]
    arquero_a_caballo_pesado = [40, 0, 60, 0, 28]
    artillero_manual = [0, 45, 50, 0, 34]

    if value == 'Ballesta':
        ret = ballesta
    if value == 'Guerrillero de Elite Imperial':
        ret = guerrillero_elite_imp
    if value == 'Arquero a Caballo Pesado':
        ret = arquero_a_caballo_pesado
    if value == 'Artillero Manual':
        ret = artillero_manual

    # Establo

    husar = [25, 35, 0, 0, 22]
    caballero = [0, 60, 75, 0, 30]
    paladin = [0, 60, 75, 0, 30]
    camello_armadura = [0, 55, 60, 0, 22]
    camello_imp = [0, 55, 60, 0, 20]
    elefante_elite = [0, 120, 70, 0, 28]

    if value == 'Husar':
        ret = husar
    if value == 'Caballero':
        ret = caballero
    if value == 'Paladin':
        ret = paladin
    if value == 'Camello con Armadura':
        ret = camello_armadura
    if value == 'Camello Imperial':
        ret = camello_imp
    if value == 'Elefante de Combate de Elite':
        ret = elefante_elite

    # Taller de maquinaria

    ariete_cubierto = [25, 35, 0, 0, 35]
    ariete_asedio = []
    onagro = [160, 0, 135, 0, 46]
    onagro_asedio = []
    escorpion_pesado = [75, 0, 75, 0, 30]
    cañon_de_asedio = [225, 0, 225, 0, 56]

    if value == 'ariete cubierto':
        ret = ariete_cubierto
    if value == 'ariete_asedio':
        ret = ariete_asedio
    if value == 'onagro':
        ret = onagro
    if value == 'onagro_asedio':
        ret = onagro_asedio
    if value == 'escorpion_pesado':
        ret = escorpion_pesado
    if value == 'cañon_asedio':
        ret = cañon_de_asedio

    return ret
