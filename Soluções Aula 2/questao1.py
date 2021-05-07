a = int(input("Digite o coeficiente A: "))
b = int(input("Digite o coeficiente B: "))
c = int(input("Digite o coeficiente C: "))

if( a == 0):
  if(b == 0):
    print("Impossível resolver")
  else:
    print("A raiz é: ", (-c) / b)

else:
  delta = (b**2) -(4*a*c)

  if delta < 0:
    print("Não existe raiz real")
  elif delta == 0:
    print("A raiz é:", (-b)/(2*a) )
  else:
    print("Raiz 1:", (-b + delta**(1/2) )/(2*a) )
    print("Raiz 2:", (-b - delta**(1/2) )/(2*a) )