from random import randint
t = ["Pedra", "Papel", "Tesoura"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Pedra, Papel ou Tesoura?")
    if player == computer:
        print("Empate!")
    elif player == "Pedra":
        if computer == "Papel":
            print("Você Perdeu!", computer, "embrulha", player)
        else:
            print("Você Ganhou!", player, "esmaga", computer)
    elif player == "Papel":
        if computer == "Tesoura":
            print("Você Perdeu!", computer, "corta", player)
        else:
            print("Você Ganhou!", player, "embrulha", computer)
    elif player == "Tesoura":
        if computer == "Pedra":
            print("Você Perdeu...", computer, "quebra", player)
        else:
            print("Você Ganhou!", player, "corta", computer)
    else:
        print("Não é uma jogada válida")
    player = False
    computer = t[randint(0,2)]