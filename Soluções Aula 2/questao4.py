n = int(input("Digite um número: "))

ehPrimo = True
i = 2

while i < n//2 + 1 and ehPrimo:
    if(n % i == 0):
        ehPrimo = False
    i += 1

if(ehPrimo):
    print(n, "é primo")
else:
    print(n, "não é primo")