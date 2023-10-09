import random

n = 0
palavras = ["capivara","mosca","comer","marcelo"]
n_escolhida = random.randint(0,3)
palavra_escolhida = palavras[n_escolhida]
letra_jogada = []
letra = 0
acertos = 0
capivara = ["_","_","_","_","_","_","_","_"]
mosca = ["_","_","_","_","_"]
comer = ["_","_","_","_","_"]
marcelo = ["<3","_","_","_","_","_","_","_","<3"]

if palavra_escolhida == "capivara":
    while True:
        letra = input("\ndigite uma letra: ")
        letra = letra.upper()
        if letra in letra_jogada:
            n += 1
        else:
            letra_jogada.append(letra)
            if letra == "C":
                capivara[0] = "C"
                acertos += 1
            elif letra == "A":
                capivara[1] = "A"
                capivara[5] = "A"
                capivara[7] = "A"
                acertos += 1
            elif letra == "P":
                capivara[2] = "P"
                acertos += 1
            elif letra == "I":
                capivara[3] = "I"
                acertos += 1
            elif letra == "V":
                capivara[4] = "V"
                acertos += 1
            elif letra == "R":
                capivara[6] = "R"
                acertos += 1
            else:
                n +=1

            if n == 0:
                print("-------------\n"+
                "|             |\n"+
                "|            \n"+
                "|            \n"+
                "|\n"+
                "|\n")
            if n == 1:
                print("-------------\n"+
                "|             |\n"+
                "|            o\n"+
                "|            \n"+
                "|\n"+
                "|\n")
            if n == 2:
                print("-------------\n"+
                "|             |\n"+
                "|            o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 3:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 4:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 5:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|\n         /"+
                "|\n")
            if n == 6:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |  \n"+
                "|           / \ \n "+
                "|\n")
        for i in capivara:
            print(i, end= " ")
        if acertos == 6:
            print("\nGANHOU!")
            break
        if n == 6:
            break
            
if palavra_escolhida == "mosca":
    while True:
        letra = input("\ndigite uma letra: ")
        letra = letra.upper()
        if letra in letra_jogada:
            n += 1
        else:
            letra_jogada.append(letra)
            if letra == "C":
                mosca[3] = "C"
                acertos += 1
            elif letra == "A":
                mosca[4] = "A"
                acertos += 1
            elif letra == "M":
                mosca[0] = "M"
                acertos += 1
            elif letra == "S":
                mosca[2] = "S"
                acertos += 1
            elif letra == "O":
                mosca[1] = "O"
                acertos += 1
            else:
                n +=1
            if n == 0:
                print("-------------\n"+
                "|             |\n"+
                "|            \n"+
                "|            \n"+
                "|\n"+
                "|\n")
            if n == 1:
                print("-------------\n"+
                    "|             |\n"+
                    "|             o\n"+
                    "|\n"+
                    "|\n"+
                    "|\n")
            if n == 2:
                print("-------------\n"+
                "|             |\n"+
                "|            o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 3:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 4:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 5:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|           /\n "+
                "|\n")
            if n == 6:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |  \n"+
                "|           / \ \n "+
                "|\n")
        for i in mosca:
            print(i, end= " ")
        if acertos == 5:
            print("\nGANHOU!")
            break
        if n == 6:
            break

if palavra_escolhida == "comer":
    while True:
        letra = input("\ndigite uma letra: ")
        letra = letra.upper()
        if letra in letra_jogada:
            n += 1
        else:
            letra_jogada.append(letra)
            if letra == "C":
                comer[0] = "C"
                acertos += 1
            elif letra == "R":
                comer[4] = "R"
                acertos += 1
            elif letra == "M":
                comer[2] = "M"
                acertos += 1
            elif letra == "E":
                comer[3] = "E"
                acertos += 1
            elif letra == "O":
                comer[1] = "O"
                acertos += 1
            else:
                n +=1
            if n == 0:
                print("-------------\n"+
                "|             |\n"+
                "|            \n"+
                "|            \n"+
                "|\n"+
                "|\n")
            if n == 1:
                print("-------------\n"+
                    "|             |\n"+
                    "|             o\n"+
                    "|\n"+
                    "|\n"+
                    "|\n")
            if n == 2:
                print("-------------\n"+
                "|             |\n"+
                "|            o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 3:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 4:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
            if n == 5:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|           /\n "+
                "|\n")
            if n == 6:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |  \n"+
                "|           / \ \n "+
                "|\n")
        for i in comer:
            print(i, end= " ")
        if acertos == 5:
            print("\nGANHOU!")
            break
        if n == 6:
            break
        

if palavra_escolhida == "marcelo":
    while True:
        letra = input("\ndigite uma letra: ")
        letra = letra.upper()
        if letra in letra_jogada:
            n += 1
        else:
            letra_jogada.append(letra)
            if letra == "C":
                marcelo[4] = "C"
                acertos += 1
            elif letra == "R":
                marcelo[3] = "R"
                acertos += 1
            elif letra == "M":
                marcelo[1] = "M"
                acertos += 1
            elif letra == "E":
                marcelo[5] = "E"
                acertos += 1
            elif letra == "O":
                marcelo[7] = "O"
                acertos += 1
            elif letra == "A":
                marcelo[2] = "A"
                acertos += 1
            elif letra == "L":
                marcelo[6] = "L"
                acertos += 1
            else:
                n +=1
                
        if n == 0:
                print("-------------\n"+
                "|             |\n"+
                "|            \n"+
                "|            \n"+
                "|\n"+
                "|\n")
        if n == 1:
            print("-------------\n"+
                "|             |\n"+
                "|             o\n"+
                "|\n"+
                "|\n"+
                "|\n")
        if n == 2:
                print("-------------\n"+
                "|             |\n"+
                "|            o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
        if n == 3:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
        if n == 4:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|\n"+
                "|\n")
        if n == 5:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |\n"+
                "|           /\n "+
                "|\n")
        if n == 6:
                print("-------------\n"+
                "|             |\n"+
                "|          \ o /\n"+
                "|            |  \n"+
                "|           / \ \n "+
                "|\n")
        for i in marcelo:
            print(i, end= " ")
        if acertos == 7:
            print("\nGANHOU!")
            break
        if n == 6:
            break