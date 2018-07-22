elegy_pokemon = input  ("¿Contra que Pokemon quieres combatir? (Squirtle / Charmander / Bulbasur)")

pikachu_hp = 100
enemy_hp = 0
pokemon_attack = 0

if elegy_pokemon == "Squirtle":
    enemy_hp = 120
    poke_name = "Squirtle"
    pokemon_attack = 30

elif elegy_pokemon == "Charmander":
    enemy_hp = 120
    poke_name = "Charmander"
    pokemon_attack = 35

elif elegy_pokemon == "Bulbasur":
    enemy_hp = 120
    poke_name = "Bulbasur"
    pokemon_attack = 40

while   pikachu_hp > 0 and enemy_hp > 0:
    elegy_attack = input("Elige movimiento (Chispazo / Trueno)")

    if elegy_attack == "Chispazo":
        enemy_hp -= 30
    elif  elegy_attack == "Trueno":
        enemy_hp -= 35
    print ("Pokemon salvaje tiene ahora {}".format(enemy_hp, poke_name))

    print ("{} te hace un ataque desconocido de {} daño".format(poke_name,pokemon_attack))
    pikachu_hp -= pokemon_attack

    print ("La vida de tu Pikachu es de {}".format(pikachu_hp))

if enemy_hp  <= 0:
    print ("¡Has ganado!")
if pikachu_hp <= 0:
    print ("¡Se acabó!")

print ("El combate ha terminado")