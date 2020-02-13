## Atividade 4

a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))

print("A ^ B:",bool(a and b))
print("A ^ C:",bool(a and c))
print("B v C:",bool(b or c))
print("A ^ B ^ C:",bool(a and b and c))
print("~A v B:",bool((not a) or b))
print("~A v ~C:",bool((not a) or (not c)))
print("(~A v B) ^ C:",bool( ((not a) or b) and c))
print("~A ^ ~B ^ ~C:",bool( (not a) and (not b) and (not c) ))
print("~(A v B v C):",bool( not(a or b or c) ))
print("A ^ False:",bool(a and False))
print("A ^ ~A:",bool(a and not(a)))
print("A v ~A:",bool(a or not(a)))