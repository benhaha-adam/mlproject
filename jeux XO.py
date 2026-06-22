"""
Jeu de Morpion (Tic-Tac-Toe) — 2 joueurs ou contre l'IA (algorithme Minimax)
Lancez avec : python morpion.py
"""

import os

def afficher(plateau):
    os.system('cls' if os.name == 'nt' else 'clear')
    symboles = {' ': '.', 'X': 'X', 'O': 'O'}
    print("\n  Morpion\n")
    for ligne in range(3):
        cellules = []
        for col in range(3):
            idx = ligne * 3 + col
            cellules.append(f" {symboles[plateau[idx]]} ")
        print("|".join(cellules))
        if ligne < 2:
            print("-----------")
    print()
    print("  Cases :")
    for ligne in range(3):
        nums = [f" {ligne * 3 + col + 1} " for col in range(3)]
        print("|".join(nums))
        if ligne < 2:
            print("-----------")
    print()


def verifier_gagnant(plateau, joueur):
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6],             # diagonales
    ]
    return any(all(plateau[i] == joueur for i in combo) for combo in combinaisons)


def est_plein(plateau):
    return all(c != ' ' for c in plateau)


def minimax(plateau, est_ia):
    if verifier_gagnant(plateau, 'O'):
        return 10
    if verifier_gagnant(plateau, 'X'):
        return -10
    if est_plein(plateau):
        return 0

    scores = []
    for i in range(9):
        if plateau[i] == ' ':
            plateau[i] = 'O' if est_ia else 'X'
            scores.append(minimax(plateau, not est_ia))
            plateau[i] = ' '

    return max(scores) if est_ia else min(scores)


def meilleur_coup(plateau):
    meilleur_score = -float('inf')
    coup = -1
    for i in range(9):
        if plateau[i] == ' ':
            plateau[i] = 'O'
            score = minimax(plateau, False)
            plateau[i] = ' '
            if score > meilleur_score:
                meilleur_score = score
                coup = i
    return coup


def jouer_contre_ia():
    plateau = [' '] * 9
    print("\nVous jouez X, l'IA joue O.")
    input("Appuyez sur Entrée pour commencer...")

    while True:
        afficher(plateau)

        # Tour du joueur
        while True:
            try:
                choix = int(input("Votre coup (1-9) : ")) - 1
                if 0 <= choix <= 8 and plateau[choix] == ' ':
                    break
                print("Case invalide ou déjà prise, réessayez.")
            except ValueError:
                print("Entrez un nombre entre 1 et 9.")

        plateau[choix] = 'X'
        afficher(plateau)

        if verifier_gagnant(plateau, 'X'):
            print("Bravo, vous avez gagné !\n")
            return

        if est_plein(plateau):
            print("Match nul !\n")
            return

        # Tour de l'IA
        print("L'IA réfléchit...")
        coup_ia = meilleur_coup(plateau)
        plateau[coup_ia] = 'O'

        if verifier_gagnant(plateau, 'O'):
            afficher(plateau)
            print("L'IA a gagné !\n")
            return

        if est_plein(plateau):
            afficher(plateau)
            print("Match nul !\n")
            return


def jouer_a_deux():
    plateau = [' '] * 9
    joueur = 'X'

    while True:
        afficher(plateau)
        print(f"Tour de {joueur}")

        while True:
            try:
                choix = int(input(f"{joueur}, choisissez une case (1-9) : ")) - 1
                if 0 <= choix <= 8 and plateau[choix] == ' ':
                    break
                print("Case invalide ou déjà prise.")
            except ValueError:
                print("Entrez un nombre entre 1 et 9.")

        plateau[choix] = joueur
        afficher(plateau)

        if verifier_gagnant(plateau, joueur):
            print(f"Le joueur {joueur} a gagné !\n")
            return

        if est_plein(plateau):
            print("Match nul !\n")
            return

        joueur = 'O' if joueur == 'X' else 'X'


def main():
    while True:
        print("\n=== MORPION ===")
        print("1. Jouer à deux")
        print("2. Jouer contre l'IA")
        print("3. Quitter")

        choix = input("\nVotre choix : ").strip()

        if choix == '1':
            jouer_a_deux()
        elif choix == '2':
            jouer_contre_ia()
        elif choix == '3':
            print("Au revoir !\n")
            break
        else:
            print("Choix invalide.")

        rejouer = input("Rejouer ? (o/n) : ").strip().lower()
        if rejouer != 'o':
            print("Au revoir !\n")
            break


if __name__ == "__main__":
    main()