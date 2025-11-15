class Grille:
    """Représente une grille de bataille navale sous forme de liste 1D."""

    def __init__(self, nombre_lignes: int, nombre_colonnes: int):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes

        # caractère pour une case vide
        self.vide = '~'

        # matrice stockée dans une seule liste de caractères
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def index(self, ligne: int, colonne: int) -> int:
        """
        Convertit (ligne, colonne) -> index dans la liste.
        Ici on utilise des coordonnées commençant à 1.
        """
        return (ligne - 1) * self.nombre_colonnes + (colonne - 1)

    def tirer(self, ligne: int, colonne: int, touche: str = 'x') -> None:
        """
        Marque un tir sur la case (ligne, colonne).
        Par défaut on utilise 'x', mais on peut personnaliser avec `touche`.
        """
        idx = self.index(ligne, colonne)
        self.matrice[idx] = touche

    def ajoute(self, bateau) -> None:
        """
        Place un bateau sur la grille en utilisant bateau.marque
        sur toutes les positions du bateau.

        Le vaisseau n'est placé que s'il est entièrement contenu dans la grille
        Si l'une des cases est en dehors de la grille, rien ne se passe.
        """
        for (l, c) in bateau.positions:
            if not (1 <= l <= self.nombre_lignes and 1 <= c <= self.nombre_colonnes):
                return

        for (l, c) in bateau.positions:
            idx = self.index(l, c)
            self.matrice[idx] = bateau.marque

    def afficher(self) -> None:
        """Affiche la grille sur la sortie standard."""
        print(self.__str__())

    def __str__(self) -> str:
        """Retourne une représentation textuelle de la grille."""
        lignes = []
        for l in range(self.nombre_lignes):
            ligne = ""
            for c in range(self.nombre_colonnes):
                ligne += self.matrice[self.index(l + 1, c + 1)]
            lignes.append(ligne)
        return "\n".join(lignes)
