# bateau.py

class Bateau:
    """
    Représente un bateau sur la grille.

    Attributs (dans l'ordre demandé) :
      - ligne : int
      - colonne : int
      - longueur : int (par défaut 1)
      - vertical : bool (par défaut False = horizontal)
    """

    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

        # marque générique pour un bateau "normal"
        self.marque = "⛵"

        # indique si ce bateau a déjà été déclaré "coulé" dans le jeu
        self.deja_coule = False

    @property
    def positions(self):
        """
        Retourne la liste des positions (ligne, colonne) occupées par le bateau.

        - si vertical == False : les colonnes augmentent (bateau horizontal)
        - si vertical == True  : les lignes augmentent (bateau vertical)
        """
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille, touche: str = '💣') -> bool:
        """
        Vérifie si le bateau est coulé sur la grille donnée.
        Il est considéré coulé si TOUTES ses cases contiennent `touche`
        (chez toi, le tir réussi est marqué par '💣').
        """
        for (l, c) in self.positions:
            idx = grille.index(l, c)
            if grille.matrice[idx] != touche:
                return False
        return True

    def __repr__(self) -> str:
        orient = "vertical" if self.vertical else "horizontal"
        return (
            f"Bateau(ligne={self.ligne}, colonne={self.colonne}, "
            f"longueur={self.longueur}, {orient}, marque={self.marque!r})"
        )


# ========= Sous-classes pour les différents types de bateaux =========

class PorteAvion(Bateau):
    """Porte-avion : longueur 4, marque spéciale."""
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"


class Croiseur(Bateau):
    """Croiseur : longueur 3."""
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "🚤"


class Torpilleur(Bateau):
    """Torpilleur : longueur 2."""
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "⛴"


class SousMarin(Bateau):
    """Sous-marin : longueur 2."""
    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
