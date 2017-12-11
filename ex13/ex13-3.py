from sys import argv

script, game, difficulty = argv
print(">>>> argv = ", repr(argv))
players = int(input("How many human players are there? "))
print(f"{players} player(s) playing {game} on the {difficulty} difficulty. Have fun!")