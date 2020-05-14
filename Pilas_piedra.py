#Piedra/Papel/Tijera                            ##########################
from collections import deque
import random

pila = deque()

inicio = True
turno = (False)
print('------------------------------------')
print('La partida no acaba hasta que ganes!')
print('------------------------------------')

while inicio:
    print('Deseas?')
    print('1. Jugar')
    print('2. Ver resultado anterior')
    print('3. Salir')
    opcion = int(input('Ingrese su opcion: '))

    if opcion == 1:
        turno = True
    if opcion == 2:
        if len(pila) > 0:
            historial = pila.pop()
            print('El resultado de la partida anterior fue: ')
            print('')
            print(f'{historial}')
        if len(pila) < 1:
            print('----------------------------------------')
            print('No hay mas resultados')

        print('--------------------------------------------')
        inicio = True


    if opcion == 3:
        inicio = False
        turno = False

        


    while turno:
        bot = random.randint(1, 3)
        print('------------------------------------')
        print('Ingresa una opcion: ')
        print('------------------------------------')
        print('             1. Piedra') 
        print('             2. Papel')
        print('             3. Tijera')
        print('------------------------------------')
        eleccion = input('Su opcion: ')
        eleccion = int(eleccion)
        if eleccion < 1 or eleccion > 3:
            print('ERROR: Ingrese un numero valido!!!!')
        



        if eleccion == 1 and bot == 1:
            print('Empate!')
            print('Ambos eligieron Piedra')
            print('')
            pila.append('Empate!, ambos eligieron Piedra.')
        
        if eleccion == 2 and bot == 2:
            print('Empate!')
            print('Ambos eligieron Papel')
            print('')
            pila.append('Empate!, Ambos eligieron Papel')


        if eleccion == 3 and bot == 3:
            print('Empate!')
            print('Ambos eligieron Tijeras')
            print('')
            pila.append('Empate!, Ambos eligieron Tijeras')



        if eleccion == 1 and bot == 2:
            print('Equipo elijio (papel)')
            print('Perdiste, papel envuelve a piedra!')
            print('')
            pila.append('Perdiste!, Equipo Eligio Papel y tu Piedra')

        
        if eleccion == 1 and bot == 3:
            print('Equipo elijo Tijeras')
            print('Tu ganas, piedra rompe tijeras!')
            print('')
            pila.append('Ganaste!, Equipo eligio Tijeras y tu Piedra')
            turno = False

        if eleccion == 2 and bot == 1:
            print('Equipo elijio (Piedra)')
            print('Tu ganas, Papel envuelve a piedra!')
            print('')
            pila.append('Ganaste!, Equipo elijio Piedra y tu Papel')
            turno = False

        if eleccion == 2 and bot == 3:
            print('Equipo elijio (Tijeras)')
            print('Perdiste, Tijeras cortan papel!')
            print('')
            pila.append('Perdiste!, Equipo eligio Tijeras y tu Papel')

        
        if eleccion == 3 and bot == 1:
            print('Equipo elijio (Piedra)')
            print('Perdiste, piedra rompe tijeras!')
            print('')
            pila.append('Perdiste, Equipo eligio Piedra y tu Tijeras')


        if eleccion == 3 and bot == 2:
            print('Equipo elijio (Papel)')
            print('Tu ganas, Tijeras cortan papel!')
            print('')
            pila.append('Ganaste!, Equipo eligio Papel y tu Tijeras')
            turno = False


 

print('Gracias por Participar')


        





