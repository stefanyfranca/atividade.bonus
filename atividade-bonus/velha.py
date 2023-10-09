linha1 = ["-","-","-"]
linha2 = ["-","-","-"]
linha3 = ["-","-","-"]

while True:
    linhax = int(input("Escolha a linha X: "))
    colunax = int(input("Escolha a coluna X: "))
    if linhax == 0:
        if colunax == 0 and linha1[0] == "-":
            linha1[0]= "X" 
        if colunax == 1 and linha1[1] == "-":
            linha1[1]= "X" 
        if colunax == 2 and linha1[2] == "-":
            linha1[2]= "X" 
    elif linhax == 1:
        if colunax == 0 and linha2[0] == "-":
            linha2[0]= "X" 
        if colunax == 1 and linha2[1] == "-":
            linha2[1]= "X" 
        if colunax == 2 and linha2[2] == "-":
            linha2[2]= "X" 
    elif linhax == 2:
        if colunax == 0 and linha3[0] == "-":
            linha3[0]= "X" 
        if colunax == 1 and linha3[1] == "-":
            linha3[1]= "X" 
        if colunax == 2 and linha3[2] == "-":
            linha3[2]= "X" 
    print(linha1)
    print(linha2)
    print(linha3)

    if linha1[0] == "X" and linha1[1] == "X" and linha1[2] == "X":
        print("X GANHOU")
        break
    if linha2[0] == "X" and linha2[1] == "X" and linha2[2] == "X":
        print("X GANHOU")
        break
    if linha3[0] == "X" and linha3[1] == "X" and linha3[2] == "X":
        print("X GANHOU")
        break
    if linha1[0] == "X" and linha2[0] == "X" and linha3[0] == "X":
        print("X GANHOU")
        break
    if linha1[1] == "X" and linha2[1] == "X" and linha3[1] == "X":
        print("X GANHOU")
        break
    if linha1[2] == "X" and linha2[2] == "X" and linha3[2] == "X":
        print("X GANHOU")
        break
    if linha1[0] == "X" and linha2[1] == "X" and linha3[2] == "X":
        print("X GANHOU")
        break
    if linha1[2] == "X" and linha2[1] == "X" and linha3[0] == "X":
        print("X GANHOU")
        break
    
    
    linhao = int(input("Escolha a linha O: "))
    colunao = int(input("Escolha a coluna O: "))
    if linhao == 0:
        if colunao == 0 and linha1[0] == "-":
            linha1[0]= "O" 
        if colunao == 1 and linha1[1] == "-":
            linha1[1]= "O" 
        if colunao == 2 and linha1[2] == "-":
            linha1[2]= "O" 
    elif linhao == 1:
        if colunao == 0 and linha2[0] == "-":
            linha2[0]= "O" 
        if colunao == 1 and linha2[1] == "-":
            linha2[1]= "O" 
        if colunao == 2 and linha2[2] == "-":
            linha2[2]= "O" 
    elif linhao == 2:
        if colunao == 0 and linha3[0] == "-":
            linha3[0]= "O" 
        if colunao == 1 and linha3[1] == "-":
            linha3[1]= "O" 
        if colunao == 2 and linha3[2] == "-":
            linha3[2]= "O" 

    print(linha1)
    print(linha2)
    print(linha3)
    if linha1[0] == "O" and linha1[1] == "O" and linha1[2] == "O":
        print("O GANHOU")
        break
    if linha2[0] == "O" and linha2[1] == "O" and linha2[2] == "O":
        print("O GANHOU")
        break
    if linha3[0] == "O" and linha3[1] == "O" and linha3[2] == "O":
        print("O GANHOU")
        break
    if linha1[0] == "O" and linha2[0] == "O" and linha3[0] == "O":
        print("O GANHOU")
        break
    if linha1[1] == "O" and linha2[1] == "O" and linha3[1] == "O":
        print("O GANHOU")
        break
    if linha1[2] == "O" and linha2[2] == "O" and linha3[2] == "O":
        print("O GANHOU")
        break
    if linha1[0] == "O" and linha2[1] == "O" and linha3[2] == "O":
        print("O GANHOU")
        break
    if linha1[2] == "O" and linha2[1] == "O" and linha3[0] == "O":
        print("O GANHOU")
        break


