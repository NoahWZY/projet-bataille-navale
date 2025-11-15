from grille import Grille


def main():
    print('User story : "Plouf dans l\'eau"')
    # 1. créer une grille à 5 lignes et 8 colonnes
    g = Grille(5, 8)

    # boucle principale
    while True:
        # 2. afficher la grille à l'écran
        print()
        print(g)
        print()

        # 3. demande à l'utilisateur de rentrer deux coordonnées
        try:
            ligne = int(input(f"Numéro de ligne (1–{g.nombre_lignes}) : "))
            colonne = int(input(f"Numéro de colonne (1–{g.nombre_colonnes}) : "))
        except ValueError:
            print("Veuillez entrer des nombres entiers.")
            continue

        # vérification simple des bornes
        if not (1 <= ligne <= g.nombre_lignes and 1 <= colonne <= g.nombre_colonnes):
            print("Coordonnées hors de la grille, recommencez.")
            continue

        # 4. tirer à l'endroit indiqué sur la grille
        g.tirer(ligne, colonne)

        # 5. retour en 2 (boucle while reprend automatiquement)


if __name__ == "__main__":
    main()
