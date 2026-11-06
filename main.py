"""
Maria Fatou Faye Maestre
404
combat des monstres
"""
import random


pv_player = 20
alive = True
augmentation = 0.5
pv_monster = random.randint(4, 20)
nb_turns = 0
names_for_monsters = ["minotaure", "cèrbère", "Meduse", "hydre de Lerne", "chimere", "sphinx", "Circe", "Jormungand"]
nom_montre = ""

def show_state(pv_player, nb_turns):
    print(pv_player)
    print(nb_turns)


def game_rules():
    print(f"Voici les règles du jeux du combats des monstres."
      f"\n Vous commencez la partie avec 20 points de vie."
      f" \n Il va vous être presenter des monstres."
      f" \n Vous pouvez choisir de les combatres ou de fuir."
      f" \n Si vous combatez et gagnez, vous gagner un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous combatez et perdez, vous perdez un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous fuyez, vous perdez 8 points de vie. "
      f"\n Si vous arrivez a survivre a 10 monstres. vous gagnez. "
      f"\n Si vous perdez tous vos points de vie, vous perdez.")


def run_away(pv_player):
    pv_player -= 8


def pv_monstre(pv_monster):
    pv_ajoute = int(pv_monster * augmentation)


def monstre_a_combatre():
    global nom_montre, pv_monster
    nom_montre = random.choice(names_for_monsters)
    pv_monster = random.randint(4, 20)
    print(f"Le monstre {nom_montre} a {pv_monster} de force.")



def fight(pv_player):

    if pv_player < pv_monster:
        pv_player -= pv_monster
    elif pv_player > pv_monster:
        pass
       # pv_player += pv_ajoute
    elif pv_player <= 0:
        alive = False




while alive and nb_turns < 10:
    #game_rules()
    monstre_a_combatre()
    nb_turns += 1
    action = input("Voulez-vous (c)ombattre ce montre, (f)uir, \n"
                   " constater votre (é)tat ou voir les (r)ègles du jeu une fois de plus ?")
    if action == "c":
        fight(pv_player)
        nb_turns += 1
    elif action ==  "f":
        run_away(pv_player)
        nb_turns += 1
    elif action == "é":
        show_state(pv_player, nb_turns)
    elif action == "r":
        game_rules
    else:
        print(f"S'il-vous-plaît répondre par l'une des quatres lettres.")




