# PROYECTO LA VITROLA MAGICA
# Proyecto Final Python Inicial

# Autor: Mario Martínez - ingenieromario@hotmail.com
# Version: 1.0

import csv
import random
from tkinter import N

# Funcion para presentación
def presentacion():
    print("==========================================")
    print("         LA VITROLA MAGICA ")
    print("==========================================")
    print("¡Bienvenidos al desafío Musical del Siglo!")
    print("==========================================")
    print("En este juego el programa reproduce 10 segundos de una canción elegida aleatoriamente 🎹 y brinda 4 opciones al usuario, quien debe elegir cuál es el nombre de la canción que se reprodujo. Preparado para 2 jugadores. Cada acierto suma 1 punto. Son 3 rondas donde van cambiando los géneros de las canciones, dicho género musical es mostrado previamente antes de escuchar la misma. Finalmente se muestra el puntaje obtenido por cada jugador, y si hubo un ganador el mismo ingresa al registro histórico de ganadores del Juego!")

# Función para pedir el nombre de un jugador
def pido_nombre(numero):
    print("Porfa ingrese el nombre del ",numero,"° jugador:")
    nom = str(input())
    return nom

# Saludo a Ambos y reglas del Juego
def saludo_reglas(j1,j2):
    print("Bienvenidos",j1,"y",j2,"!! Exitos Totales")
    print("==========================================")
    print("Se incia el juego, son 5 rondas, un turno por vez, preparados... listo... fuera!")

# Función para cargar el csv a la lista
def cargo_csv():
    archivo = 'preguntas.csv'    
    with open(archivo,'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    return data

# Función para jugada
def jugada(lista,nro_jugador,nom_jugador):
    
    print("Turno del jugador:",nro_jugador,"/",nom_jugador)
    print("Buscando aleatoriamente una canción.....")
    num_cancion = random.randint(0,6)
    print("Género de la Canción seleccionada: ",lista[num_cancion]['genero'].upper())
    input("Listo! Presione una tecla para escuchar la canción por 10 segundos y aguarde....")
    nombre_archivo = lista[num_cancion]['cancion']
    from playsound import playsound
    playsound(nombre_archivo)    
    
    # Ahora muestro las opciones
    print("Opciones disponibles:")
    print(lista[num_cancion]['respuesta_1'].upper())
    print(lista[num_cancion]['respuesta_2'].upper())
    print(lista[num_cancion]['respuesta_3'].upper())
    print(lista[num_cancion]['respuesta_4'].upper())
    #playsound(None)    
    opcion = str(input("Ingrese su opción!"))
    # Valido si la respuesta es correcta o no
    if opcion==lista[num_cancion]['respuesta_correcta']:
        print("Bravo! Respuesta Correcta !! Eres un genio musical !!")
        input("Presione enter para continuar...")
        return(1)
    else:
        print("Lo siento mucho, respuesta incorrecta! Siga capacitándose musicalmente !")    
        input("Presione enter para continuar...")
        return(0)

# Función para guardar el ganador
def write_csv(nombre_jug,puntos_jug):
    # El objetivo es abrir el archivo ganadores.csv
    # y agregar el nuevo ganador al historial    
    # Este archivo ya tiene grabado el header en
    # el archivo pero de todas formas debemos especificarlo
    header = ['nombre', 'puntos']
    # Este archivo quizá ya tiene algunos ganadores cargados, agregamos más
    # Abrir un archivo CSV con el flag "a"
    csvfile = open('ganadores.csv', 'a', newline='')
    # Generar un "escritor" para modificar el archivo
    writer = csv.DictWriter(csvfile, fieldnames=header)
    # Crear el nuevo ganador
    nuevo_ganador = {'nombre': nombre_jug, 'puntos': puntos_jug}
    # Escribirlo en el archivo
    writer.writerow(nuevo_ganador)
    # Cerrar el archivo
    csvfile.close()

# Función para Listar los ganadores
def listar_ganadores():
    archivo = 'ganadores.csv'    
    with open(archivo,'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        print("Nombre: ",data[i]['nombre'],"Puntos",data[i]['puntos'])


if __name__ == '__main__':
    presentacion()  ## Llamo a la función de presentación
    jugador_1 = pido_nombre(1)  ## Pido nombre de 1° jugador
    jugador_2 = pido_nombre(2)  ## Pido nombre de 2° jugador
    saludo_reglas(jugador_1,jugador_2)  ## Saludo a ambos jugadores y muestro las reglas
    lista_preguntas = cargo_csv()   ## Se cargan las preguntas y se genera la lista de diccionarios
    puntaje_j1 = 0  ## Inicializo variable para sumar puntaje jugador 1
    puntaje_j2 = 0  ## Inicializao variable para sumar puntaje jugador 2    
    for i in range(3):
        print("=================================")
        puntaje_j1 = puntaje_j1 + jugada(lista_preguntas,1,jugador_1)
        print("=================================")
        puntaje_j2 = puntaje_j2 + jugada(lista_preguntas,2,jugador_2)
    
    print("=================================")
    print("=================================")
    print("   RESULTADOS FINALESSSSSSS !!!")
    print("=================================")
    print("Puntaje de ",jugador_1,":",puntaje_j1)
    print("Puntaje de ",jugador_2,":",puntaje_j2)
    print("=================================")
    if puntaje_j1>puntaje_j2:
        print("Gandadorrr !! Jugador 1 !! Bravo ",jugador_1,"!!!")
        write_csv(jugador_1,puntaje_j1)
    elif puntaje_j2>puntaje_j1:
        print("Gandadorrr !! Jugador 2 !! Bravo ",jugador_2,"!!!")
        write_csv(jugador_2,puntaje_j2)
    else: 
        print("EMPATE !!!! Felicitaciones a los dos !!")

    while True:
        respuesta = str(input("Desea ver el Historial de Ganadores (Y) o Salir (N)?"))
        if respuesta.upper()=="N":
            break
        elif respuesta.upper()=="Y":
            listar_ganadores()
        else:    
            print("Respuesta incorrecta !!")
        
    print("=================================")
    print("         HASTA SIEMPRE !!!!!")
    print("=================================")
