n = int(input("Digite um número: "))

for i in range(0, n):
    if(i == 0):
        print("1 elefante incomoda muita gente!")
    elif(i % 2 == 0):
        print(i+1, "elefantes incomodam muita gente!")
    else:
        frase = str(i+1) + " elefantes "
        for j in range(0, i+1):
            frase = frase + " incomodam" 
        frase = frase + " muito mais!"
        print(frase)