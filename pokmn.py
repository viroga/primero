elegy_pokemon = input  ("¿Que Pokemon quieres combatir? (Squirtle / Charmander / Bulbasur)")

pikachu_ph = 100
enemy_hp = 0


if elegy_pokemon == "Squirtle":
    enemy_hp = 120

if elegy_pokemon == "Charmander":
    enemy_hp = 120

if elegy_pokemon   == "Bulbasur":
    enemy_hp = 120

while   pikachu_ph > 0 and enemy_ph > 0:
    elegy_attack = input("Elige movimiento (Chispazo / Trueno)")

    if elegy_attack == "Chispazo":
        enemy_hp -= 30
    if  elegy_attack  == "Trueno" :
        enemy_hp -= 35

    if elegy_pokemon == "Squirtle":
        print ("Squirtle ha atacado")
        pikachu_ph -= 30

    if elegy_pokemon == "Charmander":
        print("Charmander ha atacado")
        pikachu_ph -= 35

    if elegy_pokemon == "Bulbasur":
        print("Bulbasur ha atacado")
        pikachu_ph -= 40


print ("El combate ha terminado")