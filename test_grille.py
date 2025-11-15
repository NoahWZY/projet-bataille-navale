from grille import Grille


def test_init():
    g = Grille(3, 4)
    assert g.nombre_lignes == 3
    assert g.nombre_colonnes == 4
    assert len(g.matrice) == 12
    # toutes les cases doivent être vides au départ
    assert all(case == g.vide for case in g.matrice)


def test_index():
    g = Grille(3, 4)
    # (1,1) -> 0
    assert g.index(1, 1) == 0
    # (1,4) -> 3
    assert g.index(1, 4) == 3
    # (2,1) -> 4
    assert g.index(2, 1) == 4
    # (3,4) -> 11
    assert g.index(3, 4) == 11


def test_tirer():
    g = Grille(3, 4)
    g.tirer(2, 3)  # 2e ligne, 3e colonne
    idx = g.index(2, 3)
    assert g.matrice[idx] == 'x'


def test_affichage_vierge():
    g = Grille(2, 3)
    attendu = "...\n..."
    assert str(g) == attendu


def test_affichage_apres_tir():
    g = Grille(3, 4)
    g.tirer(2, 3)
    attendu = "....\n..x.\n...."
    assert str(g) == attendu
