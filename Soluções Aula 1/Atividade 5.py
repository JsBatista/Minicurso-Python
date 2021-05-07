## Atividade 5

print("Dados: Data de hoje: ")
dh = input("Digite o dia do mês: ")
dh = int(dh)


mh = int(input("Digite o mês: "))

ah = int(input("Digite o ano: "))


print("Dados: Data futura: ")
df = int(input("Digite o dia do mês: "))

mf = int(input("Digite o mês: "))

af = int(input("Digite o ano: "))

diasQueFaltam = ((af - ah)*360) + ((mf - mh)*30) + (df - dh)

print("Faltam", diasQueFaltam, "dias para essa data!")