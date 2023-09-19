#Declarar variables
a : float
b : float
c : float
#Pedirle al usuario que ingrese 3 números
a = float (input("Ingrese el primer número: "))
b = float (input("Ingrese el segundo número: "))
c = float (input("Ingrese el tercer número: "))
#Establecer las condiciones para determinar cuál número es mayor
#Si todos los números son iguales
if a == b == c:
    print("Los números son iguales")  
#Si hay un número mayor que el resto de números
elif a > b > c:
    print("El número "+(str)(a)+" es el mayor")
elif a < b < c:
    print("El número "+(str)(c)+" es el mayor")
else:
    print("El número "+(str)(b)+" es el mayor")


#Declarar variables
a : int
b : int
#Pedirle al usuario que ingrese 2 números
a = int (input("Ingrese el primer número: "))
b = int (input("Ingrese el segundo número: "))
#Establecer las condiciones para determinar si "a"es múltiplo de "b"
#Si el módulo entre a y b es 0
if a % b == 0:
    print((str)(a)+" es múltiplo de "+(str)(b))
#Si el módulo entre b y a es diferente de 0    
else:
    print((str)(a)+" no es múltiplo de "+(str)(b))


#Pedir al usuario que ingrese una letra
x = input("Ingrese una letra: ")
#Convertir la letra en minúscula para que no el algoritmo sea insensible a mayúsculas y minúsculas
x = x.lower()
#Verificar si el caracter ingresado es una letra y tiene una longitud de cadena de 1
if x.isalpha() and len(x) == 1:
#Verificar si la letra es una consonante o una vocal
    if x in 'aeiou':
        print((str)(x)+" es una vocal")
    else:
        print((str)(x)+" es una consonante")
else:
    print((str)(x)+" no es una letra")


#Declarar variables
Frecuencia_onda : float
#Pedir al usuario que ingrese la frecuencia de una onda
Frecuencia_onda = float(input("Ingrese la frecuencia de una onda en hz: "))
#Establecer las condiciones para determinar a qué parte del espectro pertenece la frecuencia ingresada
if Frecuencia_onda > 30.0*10**18:
    print("Rayos gamma")
elif Frecuencia_onda > 30.0*10**15:
    print("Rayos X")
elif Frecuencia_onda > 1.5*10**15:
    print("Ultravioleta extremo")
elif Frecuencia_onda > 7.89*10**14:
    print("Ultravioleta cercano")
elif Frecuencia_onda > 384*10**12:
    print("Espectro visible")
elif Frecuencia_onda > 120*10**12:
    print("Infrarrojo cercano")
elif Frecuencia_onda > 6.00*10**12:
    print("Infrarrojo medio")
elif Frecuencia_onda > 300*10**9:
    print("Infrarrojo lejano o submilimétrico")
elif Frecuencia_onda > 3*10**8:
    print("Microondas")
elif Frecuencia_onda > 300*10**6:
    print("Ultra Alta Frecuencia-Radio")
elif Frecuencia_onda > 30*10**6:
    print("Muy Alta Frecuencia-Radio")
elif Frecuencia_onda > 1.7 * 10**6:
    print("Onda Corta-Radio")
elif Frecuencia_onda > 650 * 10**3:
    print("Onda Media-Radio")
elif Frecuencia_onda > 30 * 10**3:
    print("Onda Larga-Radio")
else:
    print("Muy Baja Frecuencia-Radio")