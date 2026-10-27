"""
Maria Fatou Faye Maestre
404
combat des monstres
"""
import random


pv_player = 20
alive = True
augmentation = 0.5
pv_ajoute = int(pv_monstre * augmentation)
names_for_monsters = ["minotaure", "cerbere", "Meduse", "hydre de Lerne", "chimere", "sphinx", "Circe", "Jormungand"]
game_rules = print(f"Voici les regles du jeux du combats des monstres."
      f"\n Vous commencez la partie avec 20 points de vie."
      f" \n Il va vous etre presenter des monstres."
      f" \n Vous pouvez choisir de les combatres ou de fuir."
      f" \n Si vous combatez et gagnez, vous gagner un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous combatez et perdez, vous perdez un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous fuyez, vous perdez 8 points de vie. "
      f"\n Si vous arrivez a survivre a 10 monstres. vous gagnez. "
      f"\n Si vous perdez tousvos points de vie, vous perdez.")

def
def run_away(pv_player):
    pv_player -= 5
def fight(pv_player):
    monstre_a_combattre = random.choice(names_for_monsters)
    pv_monster = random.randint(4, 20)
    if pv_player < pv_monster:
        pv_player -= pv_monster
    elif pv_player > pv_monster:
        pv_player += pv_ajoute
    elif pv_player < 0:
        alive = False
b


while alive:
    nb_turns += 1
