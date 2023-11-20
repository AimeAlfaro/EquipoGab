
print ("******************************  MATEMATICAS  ***********************************")
print ("A continuacion te mostramos algunas opciones matematicas: ")

#Se crea el menu para seleccionar lo que se desea realizar
while True:
    print ("a - Operaciones matematicas")
    print ("b - Factorial")
    print ("c - Tablas de multiplicar")
    print ("d - Potencias")
    print ("e - Promedio")
    print ("f - Maximos y Minimos")
    print ("g - Ninguna de las anteriores")

    opcion = input("Escoja la opcion deseada: ")
    if opcion == 'g':
        break

    #Esta parte del codigo son las operaciones de Suma, Multiplicacion y Division.
    if opcion in ('a'):
        print("\nEscoja la operacion: ")
        print("1. Suma de 'n' números")
        print("2. Producto entre 'n' números")
        print("3. División entre 2 números")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            n = int(input("Ingrese la cantidad de números a sumar: "))
            numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
            resultado = sum(numeros)
            print(f"La suma de los números es: {resultado}\n")

        elif opcion == "2":
            n = int(input("Ingrese la cantidad de números a multiplicar: "))
            numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
            resultado = 1
            for num in numeros:
                resultado *= num
            print(f"El producto de los números es: {resultado}\n")

        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
    
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"La división de {num1} entre {num2} es: {resultado}\n")

#Factorizar un número indicado por el teclado.
    if opcion in ('b'):
        n = int(input("Ingresa el numero a factorizar: "))
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
       
        resultado = factorial(n)
        print("El factorial de ", n, "es: ", resultado, "\n")       
                
            
    if opcion in ('c'):
        n = int(input("Ingresa la tabla que deseas visualizar: "))
        for f in range(1, 11):
            multiplicacion = n * f
            print (f'n x {f} = {multiplicacion}')


    if opcion in ('d'):
        n = int(input("\nIngresa el numero para calcular su potencia al cuadrado y al cubo: "))
        p2 = n * n
        p3 = n * n * n
        print("La potencia al cuadrado de", n, "es: ", p2)      
        print("La potencia al cubo de", n, "es: ", p3, "\n")


    if opcion in ('e'):
        def prom(numeros):
            if not numeros:
             return 0
            return sum(numeros) / len(numeros)
        numeros = []

        while True:
            valor = float(input("Ingresa un numero (o -1 para terminar): "))

            if valor == -1:
                break
            else:
                numeros.append(valor)

        promedio = prom(numeros)
        print("\nEl promedio de los valores ingresados es: ", promedio, "\n")

    
 
    if opcion in ('f'):
        n = int(input("Ingrese la cantidad de números: "))
    
        maximo = float('-inf')
        minimo = float('inf')
        total = 0

        for _ in range(n):
            valor = int(input("Ingrese un número entero: "))
            total += 1

            maximo = max(maximo, valor)
            minimo = min(minimo, valor)
        
        print(f"\nSe introdujeron {total} valores.")
        print(f"El valor maximo es: {maximo}")
        print(f"El valor minimo es: {minimo} \n")  
    else:
        print("Escoja una opcion valida.")
    
