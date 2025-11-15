import random

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin, Bateau


# ---------- Placement aléatoire des bateaux (cachés) ----------

def placer_bateaux_aleatoirement(grille: Grille) -> list[Bateau]:
    """
    Place aléatoirement 4 bateaux (un de chaque type) sur la grille,
    sans chevauchement et sans sortir de la grille.
    La grille reste visuellement vide (que des '~') : les bateaux sont cachés.
    Retourne la liste de bateaux placés.
    """
    types_bateaux = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    bateaux: list[Bateau] = []
    positions_occupees: set[tuple[int, int]] = set()

    for cls in types_bateaux:
        candidats: list[Bateau] = []

        for vertical in (False, True):
            # bateau temporaire pour connaître sa longueur
            tmp = cls(1, 1, vertical=vertical)
            L = tmp.longueur

            max_ligne = grille.nombre_lignes - (L - 1 if vertical else 0)
            max_colonne = grille.nombre_colonnes - (L - 1 if not vertical else 0)

            for ligne in range(1, max_ligne + 1):
                for colonne in range(1, max_colonne + 1):
                    b = cls(ligne, colonne, vertical=vertical)

                    # Vérifier qu'aucune position n'est déjà occupée
                    if any(pos in positions_occupees for pos in b.positions):
                        continue

                    candidats.append(b)

        if not candidats:
            raise RuntimeError("Aucune position possible pour le bateau de type " + cls.__name__)

        b_choisi = random.choice(candidats)
        bateaux.append(b_choisi)
        positions_occupees.update(b_choisi.positions)

    return bateaux


# ---------- Boucle de jeu principale ----------

def partie():
    print("=== Jeu de bataille navale ===")
    print("La grille fait 8 lignes x 10 colonnes.")
    print("Il y a 4 bateaux à trouver et à couler.\n")

    # 1. créer la grille et placer les bateaux (cachés)
    g = Grille(8, 10)
    bateaux = placer_bateaux_aleatoirement(g)

    # tous les bateaux commencent comme "non coulés"
    for b in bateaux:
        b.deja_coule = False

    nb_coups = 0

    # 2. boucle de gameplay : continuer tant qu'au moins un bateau n'est pas coulé
    while not all(b.deja_coule for b in bateaux):
        print("\nGrille actuelle :\n")
        print(g)
        print()

        try:
            ligne = int(input(f"Ligne (1-{g.nombre_lignes}) : "))
            colonne = int(input(f"Colonne (1-{g.nombre_colonnes}) : "))
        except ValueError:
            print("Veuillez entrer des nombres entiers.")
            continue

        if not (1 <= ligne <= g.nombre_lignes and 1 <= colonne <= g.nombre_colonnes):
            print("Coordonnées hors de la grille, recommencez.")
            continue

        nb_coups += 1
        idx = g.index(ligne, colonne)
        contenu = g.matrice[idx]

        # case déjà visée ?
        if contenu in ('💣', 'x'):
            print("Vous avez déjà tiré sur cette case.")
            continue

        # 3. vérifier si on touche un bateau
        bateau_touche = None
        for b in bateaux:
            if (ligne, colonne) in b.positions:
                bateau_touche = b
                break

        if bateau_touche is None:
            # tir dans l'eau
            g.tirer(ligne, colonne, touche='x')  # 'x' = tir raté
            print("Plouf ! Rien ici…")
        else:
            # tir réussi
            g.tirer(ligne, colonne, touche='💣')
            print("Touché !")

        # 4. vérifier si des bateaux viennent d'être coulés
        for b in bateaux:
            if (not b.deja_coule) and b.coule(g):
                # révéler complètement le bateau avec sa marque
                for (l, c) in b.positions:
                    g.tirer(l, c, touche=b.marque)

                b.deja_coule = True
                print(f"Le bateau {b.__class__.__name__} est coulé !")

    # 5. partie terminée
    print("\nTous les bateaux sont coulés, bravo !")
    print(f"Vous avez gagné en {nb_coups} coups.")
    print("\nGrille finale :\n")
    print(g)


if __name__ == "__main__":
    partie()
