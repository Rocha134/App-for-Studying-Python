#Proyecto Integrador
#Francisco Rocha Juárez. A01730560

import random
import math
import sys

def cuestionario(archivo_respuestas, archivo_preguntas):
    #Leemos los archivos de preguntas y respuestas
    preguntas = open(archivo_preguntas, encoding='utf-8').readlines()
    respuestas = open(archivo_respuestas, encoding='utf-8').readlines()
    #Creamos 2 listas para almacenar los datos de cada uno
    lista_preguntas = []
    lista_respuestas = []
    #Iteramos en las lineas de preguntas y las guardamos en una lista
    cantidad_lineas_preguntas = 0
    for linea_preguntas in preguntas:
        lista_preguntas.append(linea_preguntas)
        cantidad_lineas_preguntas += 1
    #Iteramos en las lineas de preguntas y las guardamos en una lista
    cantidad_lineas_respuestas = 0
    for linea_respuestas in respuestas:
        lista_respuestas.append(linea_respuestas)
        cantidad_lineas_respuestas += 1
        
    print("¿Cuántas preguntas quiere contestar?")
    print("límite de preguntas " ,cantidad_lineas_preguntas)
    intentos = int(input())

    while intentos>cantidad_lineas_preguntas or intentos<1:
        print("¿Cuántas preguntas quiere contestar?")
        intentos = int(input())
    #Ciclo for que se hace acorde a la cantidad de intentos seleccionados por el usuario  
    resp_correctas = 0
    resp_incorrectas = 0
    for intento in range(0,intentos):
        
        indice = random.randint(0, cantidad_lineas_preguntas-1)
        print(lista_preguntas[indice])
        opciones = lista_respuestas[indice].split('$ ')
    #Imprimimos las respuestas junto con su número
        numeroPregunta = 1
        respuestaCorrecta = 0
        for opcion in opciones:
            print(numeroPregunta, end='. ')
            print(opcion.lower())
            #La opcion en mayusculas se asigna a respuesta correcta
            if opcion.isupper() == True:
                respuestaCorrecta = numeroPregunta
            numeroPregunta += 1
            
        respuestaUsuario = int(input())

        if respuestaUsuario == respuestaCorrecta:
            print('Respuesta correcta!')
            resp_correctas += 1
        else:
            print('Respuesta incorrecta')
            resp_incorrectas += 1
        #Eliminamos las preguntas y respuestas acorde al indice que ya fue utilizado   
        lista_preguntas.pop(indice)
        lista_respuestas.pop(indice)
        cantidad_lineas_preguntas -= 1
        
    print("respuestas correctas " ,resp_correctas)
    print("respuestas incorrectas " ,resp_incorrectas)

#Creamos la función para ingresar a la parte de biologia
def jugar_ciencias():
     print("Elige tu tema: (b)iología, (f)ísica) o (q)uímica")
     modalidad = input()
     while modalidad != "b" and modalidad != "f" and modalidad != "q":
         print("Escribe, b, f o q")
         modalidad = input()
     if modalidad == "b":
         archivo_respuestas = "respuestas_biologia.txt"
         archivo_preguntas = "preguntas_biologia.txt"
     elif modalidad == "f":
         archivo_respuestas = "respuestas_fisica.txt"
         archivo_preguntas = "preguntas_fisica.txt"
     elif modalidad == "q":
         archivo_respuestas = "respuestas_quimica.txt"
         archivo_preguntas = "preguntas_quimica.txt"
     #Llamamos a la función para llenar el cuestionario
     cuestionario(archivo_respuestas, archivo_preguntas)
     
#Creamos la función de suma     
def juego_suma():
    
    print("Excelente, elegiste suma. ¿Tienes idea del tema?")

    respuesta = input()
    # usamos un if para ver su respuesta
    if respuesta=="Si" or respuesta=="si" or respuesta=="SI":
        print("Fantastíco, emepezaremos de las bases")
    else:
        print("Estamos aquí para aprender")
    print("La adición es un proceso en el que combinamos números y hallamos el total, como en el ejemplo de abajo")
    print("3+4=7")
    print("Si tenemos 3 manzanas y compramos 4, combinadas tendremos 7 manzanas")
    print("Ahora algunos ejercicios para ti, ¿estás listo?")
    respuesta = input()
    # selective
    if respuesta=="Si" or respuesta=="SI" or respuesta=="si":
        print("Vamos a darle")
    else:
        print("Vamos a practicar")
    numa1 = random.randint(1,10)
    numa2 = random.randint(4,9)
    print("¿Cuánto es? ",numa1,"+",numa2)
    resultado_suma = int(input())
    # selective
    if resultado_suma==numa1+numa2:
        print("Excelente, haremos otra")
    else:
        print("Oh, esa no es. Intentemos de nuevo")
    numa1 = random.randint(1,15)
    numa2 = random.randint(2,5)
    print("¿Cuánto es? ",numa1,"+",numa2)
    resultado_suma = int(input())
    # selective
    if resultado_suma==numa1+numa2:
        print("Perfecto, dominaremos el tema")
    else:
        print("Explicaremos de nuevo, si añadimos los 2 números uno por uno, tendremos el resultado")
    numa1 = random.randint(4,10)
    numa2 = random.randint(1,20)
    print("¿Cuánto es?",numa1,"+",numa2)
    resultado_suma = int(input())
    # selective
    if resultado_suma==numa1+numa2:
        print("Eres un genio")
    else:
        print("Respuesta incorrecta")

#Definimos la función para resta
def juego_resta():
    print("Excelente, elegiste suma. ¿Tienes idea del tema?")

    respuesta = input()
    # usamos un if para ver su respuesta
    if respuesta=="Si" or respuesta=="si" or respuesta=="SI":
        print("Fantastíco, emepezaremos de las bases")
    else:
        print("Estamos aquí para aprender")
    print("La resta es un proceso en el que tomamos un número y le quitamos las unidades del otro, como en el ejemplo de abajo")
    print("10-4=6")
    print("Si tenemos 4 manzanas y regalamos 3, nos sobra 1 manzana")
    print("Ahora algunos ejercicios para ti, ¿estás listo?")
    respuesta = input()
    # selective
    if respuesta=="Si" or respuesta=="SI" or respuesta=="si":
        print("Vamos a darle")
    else:
        print("Vamos a practicar")
    numa1 = random.randint(5,10)
    numa2 = random.randint(1,4)
    print("¿Cuánto es? ",numa1,"-",numa2)
    resultado_resta = int(input())
    # selective
    if resultado_resta==numa1-numa2:
        print("Excelente, haremos otra")
    else:
        print("Oh, esa no es. Intentemos de nuevo")
    numa1 = random.randint(10,15)
    numa2 = random.randint(5,10)
    print("¿Cuánto es? ",numa1,"-",numa2)
    resultado_resta = int(input())
    # selective
    if resultado_resta==numa1-numa2:
        print("Perfecto, dominaremos el tema")
    else:
        print("Explicaremos de nuevo, si tenemos un número dado y a este le quitamos el segundo número, tendremos el resultado")
    numa1 = random.randint(20,30)
    numa2 = random.randint(7,19)
    print("¿Cuánto es?",numa1,"-",numa2)
    resultado_resta = int(input())
    # selective
    if resultado_resta==numa1+numa2:
        print("Eres un genio")
    else:
        print("Resultado incorrecto")
#Creamos la función de división      
def juego_division():
    print("Excelente, escogiste división")
    print("La división es vista como cuantas veces cabe un número en otro")
    print("Ejemplo: 8/2 ")
    print(" El resultado es 4 porque el 2 cabe cuatro veces en el 8, sabemos eso porque 2+2+2+2=8 o 2x4=8")
    print("¿Qué te parecen algunos ejercicios?")
    respuesta = input()
    # selective
    if respuesta=="Si" or respuesta=="SI" or respuesta=="si":
        print("Vamos a hacerlos")
    else:
        print("No te desanimes")
    numa1 = 8
    numa2 = 2
    print("Hagamos un ejercicio ",numa1,"/",numa2)
    resultado_division = int(input())
    # Selective
    if resultado_division==numa1/numa2:
        print("Perfecto, hagamos otra")
    else:
        print("Equivocado, practiquemos más")
    numa1 = 12
    numa2 = 4
    print("¿Cuánto es? ",numa1,"/",numa2)
    resultado_division = int(input())
    # selective
    if resultado_division==numa1/numa2:
        print("Estás que ardes")
    else:
        print("Esa no es la respuesta, repasemos, el número ",numa2," cabe ",numa1/numa2," veces en el número ",numa1," poeso ese es el resultado")
    numa1 = 24
    numa2 = 6
    print(" ¿Cuánto es? ",numa1,"/",numa2)
    resultado_division = int(input())
    # selective
    if resultado_division==numa1/numa2:
        print("Lo haces muy bien")
    else:
        print("Resultado equivocado")

#Creamos la función jugar matemáticas   
def jugar_matematicas():
    print("Selecciona una opción")
    print ("(s)uma, (r)esta, (d)ivisión")
    modalidad = input()
    #Elegimos la ve
    while modalidad != "s" and modalidad != "r" and modalidad != "d":
        print("Escribe s, r o d")
        modalidad = input()
    if modalidad == "s":
        juego_suma()
    elif modalidad == "r":
        juego_resta()
    elif modalidad == "d":
        juego_division()



print("Bienvenido a Aprende Fácil \nHoy aprenderemos mucho")

while True:
    print("Selecciona que te gustaría aprender hoy")
    print("1.Matemáticas\n2.Ciencias")
    print("O escribe exit para salir")
    #Preguntamos al usuario la modalidad
    opcion = input()
    #Comenzamos una estructura if para los distintos casos
    if opcion == str(1):
        print("Aquí practicaremos matemáticas")
        jugar_matematicas()
    elif opcion == str(2):
        print("Aquí practicaremos temas de Ciencias")
        jugar_ciencias()
    elif opcion == "exit":
        sys.exit()
    else:
        print("Escribe 1, 2 o 3")
        
    


