"""
Maria Fatou Faye Maestre
404
combat des monstres
"""
import random

PV = 20
names_for_monsters = ["minotaure", "cerbere", "Meduse", "hydre de Lerne", "chimere", "sphinx", "Circe", "Jormungand"]

print(f"Voici les regles du jeux du combats des monstres."
      f"\n Vous commencez la partie avec 20 points de vie."
      f" \n Il va vous etre presenter des monstres."
      f" \n Vous pouvez choisir de les combatres ou de fuir."
      f" \n Si vous combatez et gagnez, vous gagner 8 points de vie. "
      f"\n Si vous combatez et perdez, vous perdez un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous fuyez, vous perdez 5 points de vie. "
      f"\n Si vous arrivez a survivre a 10 monstres. vous gagnez. "
      f"\n Si vous perdez tousvos points de vie, vous perdez.")
while True:
    nb_turns += 1
    monstre_a_combattre = random.choice(names_for_monsters)
