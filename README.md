# Proyecto-Gargajito-1
Este repositorio contiene todo lo relacionado con el Taller #1.
a : float
b : float
c : float
a = float(input("Ingrese el primer número: ")) 
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: ")) 
if a == b == c:
  print(a,b,c)
else:
  if a < b < c:
    print(c)
  if a > b > c:
    print(a)  
  if a < b > c:
    print(b)
  if a == b < c :
    print(c)
  if a == b > c :
    print(a,b)
  if a > b == c :
    print(a)
  if a < b == c :
    print(b,c)
  if b > a == c :
    print(b)
  if b < a == c :
    print(a,c)
