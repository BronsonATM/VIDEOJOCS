import random
def main():
    print("¡Bienvenido a Camel: The Videogame!")
    print("Has robao un camello para poder atravesar el gran desierto del Sahara.")
    print("Los touareg quieren su camello de vuelta y te están persiguiendo. \n¡Sobrevive durante tu viaje por el desierto y escapa de los touareg!")
    done = False
    distancia_ladron = 0
    sed = 0
    cansancio_camello = 0
    distancia_nativos = -20
    numero_de_cantimploras = 3
    while not done:
        print (" A. Beber de tu cantimplora \n B. Continuar el trayecto a velocidad moderada \n C. Continuar el trayecto a full de velocidad \n D. Pasar la noche \n E. Comprobar la situación \n Q. Salir")
        opcion = input('¿Qué opción eliges? ')
        if opcion.upper() == 'Q':
            print('Has salido del juego.')
            input()
            done = True
        elif opcion.upper() == 'E':
            print('Distancia recorrida:',distancia_ladron,', Número de cantimploras:',numero_de_cantimploras,', Distancia recorrida por los touareg:',distancia_nativos)
        elif opcion.upper() == 'D':
            cansancio_camello = 0
            print ('¡Tu camello está contento!')
            distancia_nativos += random.randint(7,14)
        elif opcion.upper() == 'C':
            desplazamiento = random.randint(10,20)
            distancia_ladron += desplazamiento
            print('Has avanzado:',desplazamiento,'kilómetros')
            sed += 1
            cansancio_camello += random.randint(1,3)
            distancia_nativos += random.randint(7, 14)
            if random.randint(0, 100) <= 5:
                print('¡Has encontrado el oasis!')
                sed = 0
                cansancio_camello = 0
                numero_de_cantimploras = 3
        elif opcion.upper() == 'B':
            desplazamiento = random.randint(5,12)
            distancia_ladron += desplazamiento
            print('Has avanzado:', desplazamiento, 'kilómetros')
            sed += 1
            cansancio_camello += 1
            distancia_nativos += random.randint(7, 14)
            if random.randint(0, 100) <= 5:
                print('¡Has encontrado el oasis!')
                sed = 0
                cansancio_camello = 0
                numero_de_cantimploras = 3
        elif opcion.upper() == 'A':
            if numero_de_cantimploras>0:
                numero_de_cantimploras -=1
                sed = 0
                print('Glugluglu')
            else:
                print('No te queda agua')
        else:
            print('Por favor, introduzca una opción correcta.')
        if distancia_ladron >= 200:
            print('¡Enhoranuena, has ganado el juego!')
            input()
            done = True
        if sed == 4:
            print('Tienes sed amigo.')
        elif sed == 5:
            print('Tienes mucha sed amigo.')
        elif sed >= 6:
            print('Te has muerto deshidratado. Has perdido el juego :(.')
            input()
            done = True
        if cansancio_camello==5:
            print('Tu camello se está cansando.')
        elif cansancio_camello==6:
            print('Tu camello se está cansando mucho.')
        elif cansancio_camello==7:
            print('¡Tu camello se va a morir!')
        elif cansancio_camello >= 8:
            print('Tu camello se ha muerto. Los touareg te pillan y te matan. Has perdido el juego.')
            input()
            done = True
        if distancia_ladron-distancia_nativos <= 15:
            print('¡Los touareg se están acercando!')
        elif distancia_ladron - distancia_nativos <=0:
            print('Te han pillado los touareg. Te matan. Has perdido.')
            input()
            done = True
main()