n = int(input("Digite um número: "))

for i in range(1, n+1):
    if(i == 1):
        print("1 elefante incomoda muita gente!")
    elif(i % 2 != 0):
        print(i, "elefantes incomodam muita gente!")
    else:
        frase = str(i) + " elefantes"
        for j in range(0, i):
            frase = frase + " incomodam" 
        frase = frase + " muito mais!"
        print(frase)

