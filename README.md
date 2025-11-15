# Projet : Bataille Navale (Python – Programmation Objet)

Ce projet implémente une version simplifiée du jeu **Bataille Navale** en mode texte.  
Il a été réalisé dans le cadre du cours d’informatique (ECM – Programmation Objet).

---

## 🎯 Objectifs pédagogiques

Le projet permet de mettre en pratique :

- la programmation orientée objet (classes, attributs, méthodes, héritage),
- la gestion d’un environnement virtuel Python,
- l’écriture de tests unitaires avec `pytest`,
- l’utilisation d’un système de gestion de versions (Git),
- la rédaction de commits réguliers contenant un `?` (exigence du cours).

---

## 📦 Structure du projet

projet-bataille-navale/
│
├── grille.py # Classe Grille : stockage, tir, affichage
├── bateau.py # Classe Bateau + sous-classes (PorteAvion, Croiseur…)
├── main.py # Boucle principale du jeu
│
├── test_grille.py # Tests unitaires de la grille
├── test_bateau.py # Tests unitaires des bateaux
│
├── story_grille.py # User story "Plouf dans l’eau"
├── story_bateau.py # User story "Chevauchement"
│
├── requirements.txt
└── .gitignore
