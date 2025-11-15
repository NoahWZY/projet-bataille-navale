# test_bateau.py

from bateau import Bateau


def test_defauts():
    """Tester que les paramètres par défaut sont bien pris en compte."""
    b = Bateau(2, 3)   # longueur=1, vertical=False par défaut
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False


def test_positions_horizontales():
    """Tester les positions pour un bateau horizontal."""
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]


def test_positions_verticales():
    """Tester les positions pour un bateau vertical."""
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]
