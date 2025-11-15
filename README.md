# 🚢 Bataille navale — Jeu en ligne de commande (Projet Python)

Bienvenue dans **Bataille navale**, un mini-jeu classique réalisé dans le cadre du cours *Programmation Objet (ECM)*.  
Le jeu se joue entièrement dans le terminal et utilise plusieurs classes Python (Grille, Bateau, etc.).

---

## ⚡ Démarrage rapide

```bash
python main.py
```

---

## 📘 Introduction

Ce projet implémente une version simplifiée du jeu **Battleship**, jouée sur une grille de  
**8 lignes × 10 colonnes**, dans laquelle **4 bateaux** sont placés aléatoirement (non visibles au départ) :

- Porte-avion 🚢 — longueur 4  
- Croiseur 🚤 — longueur 3  
- Torpilleur ⛴ — longueur 2  
- Sous-marin 🐟 — longueur 2  

Le joueur entre des coordonnées pour tirer et tente de couler tous les bateaux avec un minimum de coups.

---

## ✨ Fonctionnalités du jeu

### 🌊 Fonctions principales

- Grille de **8 × 10**
- Placement aléatoire des bateaux sans chevauchement
- Les bateaux sont **invisibles au début**
- Mise à jour dynamique de la grille après chaque tir
- Messages :
  - `Touché !` lorsqu’un tir touche un bateau
  - Message personnalisé lorsque le bateau est **coulé**
- Affichage final :
  - Tous les bateaux coulés
  - Nombre total de tirs effectués

---

## 🎮 Symboles utilisés

| Symbole | Signification |
|--------|---------------|
| `~`    | Mer non explorée |
| `x`    | Tir dans l’eau |
| `💣`   | Tir ayant touché un bateau |
| 🚢 🚤 ⛴ 🐟 | Bateau coulé (affiché entièrement) |

---

## 🖥️ Exemple d’exécution

```
Grille actuelle :

~~💣~~~~~~~
~~~~x~~~~~
~~~~~🚤~~~
~~~~~🚤~~~
~~~~~🚤~~~
~~~~~~~~~~

Ligne (1-8) : 4
Colonne (1-10) : 6
Touché !

Le bateau Croiseur est coulé !

Tous les bateaux sont coulés !
Nombre total de coups : 23
```

---

## 🔧 Installation et exécution

### 1️⃣ Créer un environnement virtuel

```bash
python -m venv .venv
```

### 2️⃣ Activer l’environnement

**Windows :**
```bash
.venv\Scripts\activate
```

**macOS / Linux :**
```bash
source .venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer le jeu

```bash
python main.py
```

---

## 🧪 Tests (pytest)

Le projet inclut des tests unitaires et des “user stories” :

- `test_grille.py` — tests de la classe **Grille**
- `test_bateau.py` — tests des classes **Bateau**
- `story_grille.py` — story : *Plouf dans l’eau*
- `story_bateau.py` — story : *Chevauchement*

Lancer tous les tests :

```bash
pytest
```

---

## 🗂️ Structure du projet

```
projet-bataille-navale/
│
├── grille.py          # Logique de grille, tirs, affichage
├── bateau.py          # Classes Bateau et sous-classes
├── main.py            # Boucle principale du jeu
│
├── story_grille.py    # User story : tir dans l'eau
├── story_bateau.py    # User story : chevauchement
│
├── test_grille.py     # Tests unitaires Grille
├── test_bateau.py     # Tests unitaires Bateau
│
├── requirements.txt
└── .gitignore
```

---

## 🧰 Exigences du projet (ECM)

Ce projet respecte les consignes :

- Utilisation d’un **environnement virtuel**
- Présence de **tests** (pytest)
- Utilisation d’un **SCM (Git)**
- Commits réguliers (dont un avec un `?`)
- Fichiers exigés :
  - `.gitignore`
  - `README.md`
  - `requirements.txt`
  - scripts + tests

---

## 🎓 Crédit

Projet académique — *École Centrale de Marseille*, 2025.


