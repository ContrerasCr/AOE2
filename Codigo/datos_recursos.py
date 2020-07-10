
# Madera[0] Oro[1] Piedra[2] Granjas[3] Ovejas[4] Bayas[5] Caza[6] Pescadores[7]
t_prod_x_10_unid = [25, 26, 27, 28, 30, 32, 25]

# valores posibles
# edificio = tec_mad, tec_oro, tec_pie
# tec = aem, feu, cast, imp
# civ = Cualquier civilizacion


def produccion_x_seg(tec, civ):

    prod_x_seg = [0.39, 0.38, 0.36, 0.36, 0.33, 0.31, 0.41, 0.43]
    mej_civ = mej_civs(civ)
    mej_eco, _ = mej_civ
    # mejora tecnologica
    mad = tec_recursos('tec_mad', tec[0])
    oro = tec_recursos('tec_oro', tec[1])
    pie = tec_recursos('tec_pie', tec[2])

    mej_tec = [mad, oro, pie, 0, 0, 0, 0, 0]

    prod_total = [mej_tec[i] + mej_eco[i] for i in range(len(prod_x_seg))]

    nueva_prod = [round(prod_x_seg[i] * prod_total[i], 2) for i in range(len(prod_x_seg))]

    return nueva_prod
    # Return [madera, oro, piedra, alimento _______]


def tec_recursos(edificio, tec):

    ret = 0

    tec_tc = {'carretilla': 25,
              'carro_de_mano': 50}
    tec_mad = {'aem': 0,
               'feu': 0.20,
               'cast': 0.40,
               'imp':  0.50}
    tec_mol = {'aem': 0,
               'feu': 0,
               'cast': 0,
               'imp': 0}
    tec_oro = {'aem': 0,
               'feu': 0.15,
               'cast': 0.30}
    tec_pie = {'aem': 0,
               'feu': 0.15,
               'cast': 0.30}

    if edificio == 'tec_tc':
        ret = tec_tc[tec]
    if edificio == 'tec_mad':
        ret = tec_mad[tec]
    if edificio == 'tec_mol':
        ret = tec_mol[tec]
    if edificio == 'tec_oro':
        ret = tec_oro[tec]
    if edificio == 'tec_pie':
        ret = tec_pie[tec]

    return ret


def mej_civs(name):

    # ([Mejora economica], [Mejora velocidad])
    # mejora tecnologica
    # Madera[0] Oro[1] Piedra[2] Granjas[3] Ovejas[4] Bayas[5] Caza[6] Pescadores[7]
    # [1, 1, 1, 1, 1, 1, 1, 1]
    # Mejora velocidad de produccion
    # Cuartel, Arqueria, Establo, Taller, Castillo

    civ = ['aztecas', 'celtas', 'coreanos', 'eslavos', 'francos', 'godos','hunos', 'ingleses', 'mongoles', 'turcos']

    if name in civ:
        pass
    else:
        name = 'sin_mej'

    buff = {'aztecas': ([1, 1, 1, 1, 1, 1, 1, 1], [1.15, 1.15, 1.15, 1.15, 1.15]),
            'celtas': ([1.15, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1.2, 1]),
            'coreanos': ([1, 1, 1.20, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
            'eslavos': ([1, 1, 1, 1.15, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
            'francos': ([1, 1, 1, 1, 1, 1.25, 1, 1], [1, 1, 1, 1, 1]),
            'godos': ([1, 1, 1, 1, 1, 1, 1, 1], [1.2, 1, 1, 1, 1]),
            'hunos': ([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1.2, 1, 1]),
            'ingleses': ([1, 1, 1, 1, 1, 1.20, 1, 1], [1, 1.2, 1, 1, 1]),
            'mongoles': ([1, 1, 1, 1, 1, 1, 1.50, 1], [1, 1, 1, 1, 1]),
            'turcos': ([1, 1.20, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
            'sin_mej': ([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1])}

    civ = buff[str(name)]

    return civ
