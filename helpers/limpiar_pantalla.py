from os import system, name

def limpiar_pantalla():

    # windows
    if name == 'nt':
        _ = system('cls')
    # mac, linux
    else:
        _ = system('clear')
