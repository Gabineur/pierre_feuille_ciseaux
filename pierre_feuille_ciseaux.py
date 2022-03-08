import random

while True :
    action_joueur = input("Entrer votre choix (pierre, feuille, ciseaux): ")
    actions_possibles = ["pierre","feuille","ciseaux"]
    action_ordinateur = random.choice(actions_possibles)

    print(f"\nVous avez joué {action_joueur}, l'ordinateur a joué {action_ordinateur}.\n")

    if action_joueur == action_ordinateur :
        print(f"Vous avez tous les deux choisis {action_joueur}, c'est un match nul !\n")
    elif action_joueur == "pierre" :
        if action_ordinateur == "feuille":
            print("La feuille se pose sur la pierre, c'est perdu !\n")
        else :
            print("La pierre casse le ciseaux, c'est gagné !\n")
    elif action_joueur == "feuille":
        if action_ordinateur == "pierre":
            print("La feuille se pose sur la pierre, c'est gagné !\n")
        else :
            print("Le ciseaux découpe la feuille, c'est perdu !\n")
    elif action_joueur == "ciseaux":
        if action_ordinateur == "feuille":
            print("Le ciseaux découpe la feuille, c'est perdu !\n")
        else :
            print("La pierre casse le ciseau, c'est perdu !\n")
    else :
        print("CE CHOIX N'EST PAS DISPONIBLE\n")

    rejouer = input("Rejouer ? (o/n) :")
    if rejouer.lower() != "o" :
        break