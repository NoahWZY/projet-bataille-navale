# story_bateau.py

from bateau import Bateau


def chevauchent(b1: Bateau, b2: Bateau) -> bool:
    """Retourne True si les deux bateaux ont au moins une position commune."""
    return bool(set(b1.positions) & set(b2.positions))


def main():
    print('User story : "chevauchement"')
    print()

    # --- Cas 1 : deux bateaux qui se chevauchent ---
    b1 = Bateau(2, 3, longueur=3)       # [(2,3), (2,4), (2,5)]
    b2 = Bateau(2, 4, longueur=2)       # [(2,4), (2,5)]

    print("Bateaux b1 et b2 :")
    print("  b1.positions =", b1.positions)
    print("  b2.positions =", b2.positions)
    print("  Se chevauchent ? ->", chevauchent(b1, b2))
    print()

    # --- Cas 2 : deux bateaux qui ne se chevauchent pas ---
    b3 = Bateau(1, 1, longueur=2)                 # [(1,1), (1,2)]
    b4 = Bateau(3, 3, longueur=3, vertical=True)  # [(3,3), (4,3), (5,3)]

    print("Bateaux b3 et b4 :")
    print("  b3.positions =", b3.positions)
    print("  b4.positions =", b4.positions)
    print("  Se chevauchent ? ->", chevauchent(b3, b4))


if __name__ == "__main__":
    main()
