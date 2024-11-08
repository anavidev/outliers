import os

# pressionar teclas determinadas
def pressionar_tecla(valor):
    tecla = ''
    while tecla != valor:
        tecla = input(f"\n\nPressione '{valor}' para continuar\n").upper()


# limpar tela do terminal
def limpar():
    if os.name == 'nt':  # para windows
        os.system('cls')
    else:  # para linux e mac
        os.system('clear')


# imprimir itens que estao dentro de uma lista
def imprimir_lista(lista):
    for i in lista:
        print(f'{i:.2f}',end='   ')        
        
