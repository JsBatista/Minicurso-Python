n = int(input("Digite um número: "))

ant1 = 1
ant2 = 1

for i in range(0, n):
    if i <= 1:
        print("1")
    else:
        print(ant1+ant2)
        temp = ant1
        ant1 = ant1 + ant2
        ant2 = temp