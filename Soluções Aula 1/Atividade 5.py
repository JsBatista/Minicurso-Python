## Atividade 5

print("Dados: Data de hoje: ")
dh = int(input("Digite o dia do mês: "))

mh = int(input("Digite o mês: "))

ah = int(input("Digite o ano: "))


print("Dados: Data futura: ")
df = int(input("Digite o dia do mês: "))

mf = int(input("Digite o mês: "))

af = int(input("Digite o ano: "))

diasQueFaltam = ((af - ah)*365) + ((mf - mh)*20) + (df - dh)

print("Faltam", diasQueFaltam, "dias para essa data!")