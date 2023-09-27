# Proyecto-Gargajito-1
Para este repositorio, utilizamos la extensión Code Snap para poder tomarle fotos a nuestros códigos y que se vieran más bonitos. Por otro lado, los diagramas de flujo los desarrollamos para los puntos 3 y 4 debido a que ambos documentos de identidad terminaban en 3.
Espero que te guste este repositorio y si lo estas usando de guia, por lo menos deja una estrellita :).

+ **Quiz David Felipe Python Beginner Quiz (20 preguntas).**
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/3d6e2dba-dd8d-4768-9552-184dbe207050)

+ **Quiz Caterin Sierra Python Beginner Quiz (20 preguntas).**
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/d704c40f-4605-4823-a580-d1131add93f5)

## Puntos pares
+ **Realice un programa que lea tres números reales y determine cuál es el mayor.**

  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/4b7d3670-f038-4fa7-a59e-24a57a5cfd44)
 En este ejercicio, comenzamos declarando las variables como tipo 'float' para indicar que los tres números ingresados por el usuario pueden tomar valores del conjunto de los reales. A continuación, establecimos cuatro condiciones para determinar la salida según las siguientes situaciones:
  1. Si todos los números son iguales.
  2. Si el primer número (a) es mayor que los otros dos números (b y c).
  3. Si el tercer número (c) es mayor que los otros dos números (a y b).
  4. En cualquier otro caso, en el cual necesariamente el segundo número (b) es mayor que los otros dos números (a y c).
  Es importante destacar que el ejercicio no aborda situaciones en las que dos números sean iguales y también sean mayores o menores que el tercer número. Por ejemplo, si a=b>c, en ese caso, la salida sería 'a' ya que a es igual a b. El ejercicio se centra únicamente en determinar cuál de los tres números es el mayor, sin considerar casos de igualdad entre dos de ellos.
+ **Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.**

  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/60e69457-ab19-4f01-8365-abf23ad22230)
  En este ejercicio, comenzamos declarando las variables como tipo 'float' para indicar que los tres números ingresados por el usuario pueden tomar valores del conjunto de los números reales. En cuanto a la lógica del algoritmo, hemos establecido dos condiciones para determinar la salida:
  1. La primera condición se cumple cuando 'a' (el primer número) es múltiplo de 'b' (el segundo número). Esto ocurre si el residuo de la división 'a/b' es igual a cero.
  2. La segunda condición se aplica a los casos en los que el residuo de la división 'a/b' es diferente de cero, lo que indica que 'a' no es múltiplo de 'b'.
  Este algoritmo permite determinar si un número es múltiplo de otro al utilizar la propiedad fundamental de que cuando dos números son múltiplos, su división arrojará un residuo igual a cero.
   
   **_Diagrama de flujo_**

     ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/5edba27b-13c9-45bd-91cf-9bb5174c4c9c)

+  **Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.**

  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/c3dd4ed6-8a51-46fe-8a76-ba30c5ff1f22)
  En este caso, se solicita al usuario que ingrese un carácter. El algoritmo valida la entrada de usuario de la siguiente manera:
  Si el usuario ingresa un carácter que no es una letra, el algoritmo le informa que la entrada no es una letra. Además, el algoritmo establece como condición que el carácter ingresado debe tener una longitud de cadena igual a 1. Esto significa que si se ingresan varios caracteres, incluso si son letras, el algoritmo indicará que la entrada no es una letra.
  Una vez que se ha verificado que la entrada es una única letra, el algoritmo procede a determinar si es una vocal o una consonante. Esto se hace comprobando si el carácter está entre las vocales del alfabeto ('a', 'e', 'i', 'o', 'u'). Si el carácter está en este conjunto, el algoritmo informará al usuario que se trata de una vocal; de lo contrario, indicará que es una consonante.
  Es importante destacar que este algoritmo no distingue entre letras en mayúsculas o minúsculas, ya que convierte la entrada en minúsculas (x.lower) para asegurarse de que las condiciones se cumplan correctamente.
+ **Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro magnético se encuentra.**
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/4528f85d-8879-407a-98fe-00e5836f7dae)
  En este contexto, comenzamos declarando una variable para presentar frecuencia de onda como tipo "float", debido a que este dato puede tomar cualquier valor dentro del conjunto de los reales. Luego, solicitamos al usuario que ingrese la frecuencia de onda en hertzios (Hz) y en base al intervalo en el que se encuentra esa frecuencia, según la <a href="https://es.wikipedia.org/wiki/Espectro_electromagn%C3%A9tico">Tabla de Bandas del Espectro Electromagnético</a>, se determina en qué parte del espectro electromagnético se encuentra esa frecuencia de onda. 
+ **Escriba un programa que dada una distancia calcule:**
  * **_El tiempo que le tomaría a la luz recorrer la distancia._**
  * **_El tiempo que le tomaría al sonido (en el aire) recorrer la distancia._**
  * **_El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia._**
  * **_El tiempo que le tomaría a Bolt recorrer la distancia._**
  
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/9a501af8-62fd-482c-a8c4-2725ed105124)
  En esta sección, primero declaramos las variables y les asignamos el tipo de dato float para representar números reales. Luego, inicializamos las variables asignando a cada entidad (luz, sonido, Bolt y el SSC) su velocidad correspondiente en metros por segundo (m/s). Posteriormente, calculamos el tiempo que le tomaría a cada entidad recorrer la distancia proporcionada por el usuario. Esto se calcula teniendo en cuenta que cada entidad recorre ciertos metros en un segundo. Finalmente, mostramos los tiempos necesarios para que cada entidad recorra esa distancia.
## Puntos impares

+ **Realice un programa que lea un número enteros y determine si es par o impar.**
  
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/658534d7-30d4-4019-b158-ec78d73d167f)

  Este punto, fue sencillo de realizar, lo primero fue declarar las variables para que el usuario pueda ingresar un numero y por ultimo le pedimos al progrma que si l asginación con residuo es =0 nos imprina que es par, sino, que nos imprima si es impar.
  

  **_Diagrama de flujo_**


  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/875c3416-f559-48d4-a51d-5af6c6f6b97f)


+ **Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.**
  
  
![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/a81215b2-19e2-4fc9-9d76-1f98337856a7)


En este caso lo primero que hicimos fue  la declaración de variables; después, se le pidió al usuario que ingresara los tres números para la ejecución del código. Después, en las operaciones, el programa tiene que sumar los dos primeros números y evaluar si el resultado es menor, igual o mayor al tercer número e imprimir la respuesta correspondiente según la condición que se cumpla.

+ **Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:**
  * **_El promedio._**
  * **_La mediana._**
  * **_El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)._**
  * **_Ordenar los números de forma ascendente._**
  * **_Ordenar los números de forma descendente._**
  * **_La potencia del mayor número elevado al menor número._**
  * **_La raíz cúbica del menor número._**
  

  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/6f762701-cc3a-4cf0-a330-8bfc6b758be6)
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/0d88b162-03dc-48da-acaa-589562db1091)
  

+ **Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.**
  
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/dcd5d5c4-4cbb-435a-b43c-7aee1ed5a22d)
  ![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/142174506/8850525a-d061-4e53-a7fa-24f1b8009445)
  

Para ese punto, lo primero que hicimos fue declarar las variables y pedirle al usuario el ingresara de datos. Hay que tener que en cuenta que sólo se pueden ingresar los nombres de los países en minúscula, sin tíltes, ni comas, ni comillas, de lo contrario, el programa le arrojará "país no identificado". Luego de ingresar los datos, el código evaluará si está dentro de los casos posibles y así mismo, arrojará una respuesta. Como se puede observar en el código, hay muchos casos posibles, debido a que están todos los paises que conforman el continente americano.

**¡Muchas Gracias! Y RECUERDA TOMAR AGUITA Y DARLE LIKE A NUESTRO VÍDEO**

<a href="https://youtu.be/V_VHunb9EcY?si=OZso2ywMuHqIAOiM"> Videito </a>

[[![image](https://github.com/Cate1911/Proyecto-Gargajito-1/assets/141857246/2f9523bb-ee74-4f61-a7f5-3f864ae13a66)](https://open.spotify.com/intl-es/track/2VCSO1mqWPALcPbEQwgSd3?si=8a435d63fae64e24)
