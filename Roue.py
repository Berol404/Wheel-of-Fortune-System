
import random
import time

races = [
    "Humain", "Elfe", "Orc", "Gnome", "Nain", "Gobelins", "Minotaure",
    "Satyr", "Ombraux", "Céleste", "Lycanthrope", "Féliothrope",
    "Sémurien", "Skaven", "Triton", "Amibi", "Sylvestre"
]

atouts = [
    "Vision nocturne", "Régénération lente", "Résistance au feu",
    "Furtivité accrue", "Respiration aquatique", "Aura sacrée",
    "Cri terrifiant", "Camouflage naturel", "Rage temporaire",
    "Télépathie faible", "Double saut", "Sens olfactif développé"
]

armes = [
    "Épée courte", "Épée longue", "Dague", "Hache", "Marteau de guerre",
    "Lance", "Hallebarde", "Arc", "Arbalète", "Fronde",
    "Javelot", "Sarbacane", "Fouet", "Chakram", "Trident",
    "Griffe naturelle", "Poings renforcés", "Bâton magique",
    "Orbe", "Grimoire", "Sceptre", "Totem", "Aucune arme"
]

intelligence = [
    "Très faible", "Faible", "Moyenne", "Bonne", "Élevée", "Genie"
]

vitesses = [
    "Très lent", "Lent", "Normal", "Rapide", "Très rapide", "Supersonique"
]

faiblesses = [
    "Peur du feu", "Peur de l’eau", "Sensible à la magie",
    "Faible de jour", "Faible de nuit", "Maladresse",
    "Rage incontrôlable", "Vision réduite", "Faible endurance",
    "Bruyant", "Peur des hauteurs", "Malchance chronique",
    "Sensible au froid", "Sensible à la chaleur",
    "Mana instable", "Corps lourd", "Lent à réagir",
    "Instabilité mentale", "Besoin de dormir souvent"
]

def tourner(texte):
    print(texte, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def tirer_personnage():
    tourner("La roue tourne")

    race = random.choice(races)
    atout1, atout2 = random.sample(atouts, 2)
    arme = random.choice(armes)
    intel = random.choice(intelligence)
    vitesse = random.choice(vitesses)
    faiblesse = random.choice(faiblesses)

    print("PERSONNAGE GÉNÉRÉ")
    print("-------------------")
    print(f"Race         : {race}")
    print(f"Atouts       : {atout1}, {atout2}")
    print(f"Arme         : {arme}")
    print(f"Intelligence : {intel}")
    print(f"Vitesse      : {vitesse}")
    print(f"Faiblesse    : {faiblesse}")
    print("-------------------\n")


print(" JEU DE ROUE DE CRÉATION DE PERSONNAGE \n")

while True:
    input("Appuie sur ENTRÉE pour faire tourner la roue...")
    tirer_personnage()

    choix = input("Rejouer ? (o/n) : ").lower()
    if choix != "o":
        print("\nFin de la création. À bientôt ")
        break