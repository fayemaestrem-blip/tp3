"""
Maria Fatou Faye Maestre
404
combat des monstres
"""
import random



alive = True
playing = True

augmentation = 0.5
pv_monster = None
pv_player = 20
nb_turns = 0
nb_plays = 0
pv_ajoute = None
names_for_monsters = ["minotaure", "cèrbère", "Meduse", "hydre de Lerne", "chimere", "sphinx", "Circe", "Jormungand"]
nom_monstre_rn = ""

def show_state(pv_player, nb_turns):
    print(f"Vos points de vie s'élève à {pv_player}. ")
    print(f"Le nombre de tours joués est de {nb_turns}. \n")


def game_rules():
    print(f"Voici les règles du jeux du combats des monstres."
      f"\n Vous commencez la partie avec 20 points de vie."
      f" \n Il va vous être présenter des monstres."
      f" \n Vous pouvez choisir de les combatres ou de fuir."
      f" \n Si vous combatez et gagnez, vous gagner un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous combatez et perdez, vous perdez un nombre de point de vie dependant de la force du monstre. "
      f"\n Si vous fuyez, vous perdez 8 points de vie. "
      f"\n Si vous arrivez a survivre a 10 monstres, vous gagnez même si vous avez fuit. "
      f"\n Si vous perdez tous vos points de vie, vous mourez.\n")


def run_away(pv_player):
    print(f"Vous perderez donc 8 points de vie.\n")
    pv_player -= 8
    return pv_player
# Pourquoi est-ce que cette fonction ne marche pas dans la boucle while?


def pv_monstre(pv_monster):
    global pv_ajoute
    pv_ajoute = int(pv_monster * augmentation)
    return pv_ajoute



def monstre_a_combatre():
    global nom_monstre_rn, pv_monster
    nom_monstre_rn = random.choice(names_for_monsters)
    pv_monster = random.randint(4, 20)
    print(f"Le monstre {nom_monstre_rn} a {pv_monster} de force.\n")
    return nom_monstre_rn, pv_monster
# Comment faire en sorte que le monstre à combatre ne change pas si le joueur invoque l'état ou les règles?


def fight(pv_player, zero):
    if pv_player < pv_monster:
        print(f"Le monstre est plus fort que vous.\n")
        pv_player -= pv_monster
    elif pv_player > pv_monster:
        print(f"Le monstre est plus faible que vous.\n")
    pv_player += pv_ajoute
    elif pv_player < 0:
    print(f"Vos points de vie sont plus petit ou égal à zéro.\n"
          f"Vous avex perdu.\n")
        alive = False
# Pourquoi est-ce que cette fonction ne marche pas dans la boucle while?




game_rules()
while playing:
    nb_plays += 1
    while alive and nb_turns < 10:

        monstre_a_combatre()

        action = input("Voulez-vous (c)ombattre ce montre, (f)uir, \n"
                       " constater votre (é)tat ou voir les (r)ègles du jeu une fois de plus ?\n")
        if action == "c":
            fight(pv_player)
            nb_turns += 1
        elif action == "f":
            run_away(pv_player)
            nb_turns += 1
        elif action == "é":
            show_state(pv_player, nb_turns)
        elif action == "r":
            game_rules()
        else:
            print(f"S'il-vous-plaît répondre par l'une des quatres lettres entre parenthèse.\n"
                  f"(c)ombatre, (f)uir, voir les (r)ègles ou voir votre (é)tat")
choix = input(f"Voulez-vous rejouez une autre partie? oui ou non")
if choix == "oui":
    print(f"La partie va donc recommencer.")
elif choix == "non":
    print(f"Vous avez joué {nb_plays} parties.\n"
          f"Merci d'avoir joué!")
    playing = False