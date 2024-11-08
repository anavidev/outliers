from funcoes_outliers import *
from random import uniform as uni, randint as rt

# menu para comecar o programa
limpar()
pressionar_tecla('S')


# configuracoes de parametros para definir condicoes do algoritmo
limpar()
menor = 0
maior = 0

tamanho = int(input("Quantos números a lista deve ter? "))

while maior <= menor:
    menor = float(input("Defina o menor número: "))
    maior = float(input("Agora, defina o maior número: "))    


# definir numeros 'aleatorios' que estarao na lista e adicionar outliers
limpar()
itens = []

while len(itens) < tamanho:
    num_aleatorio = rt(1,tamanho)
    if num_aleatorio % 2 == 0:
        itens.append(uni(menor,maior))
    else:
        itens.append(uni((menor * num_aleatorio), (maior * num_aleatorio)))        

print(f"""
Quantidade de números: {tamanho}
Intervalo: De {menor:.2f} a {maior:.2f}""")

print("\nOs números aleatórios são: ")
imprimir_lista(itens)

pressionar_tecla('E')


# aplicacao do metodo do intervalo interquartil
limpar()
lista_organizada = sorted(itens)
qtd_itens = len(lista_organizada)

print("Números organizados em ordem crescente: ")
imprimir_lista(lista_organizada)

q1 = lista_organizada[int(qtd_itens * 0.25)]
q3 = lista_organizada[int(qtd_itens * 0.75)] 
iqr = q3 - q1

print(f'\n\nQ1 (Quartil 1): {q1:.2f}\nQ3 (Quartil 3): {q3:.2f}\nIQR (Intervalo Interquartil): {iqr:.2f}')

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f'\nLimite inferior: {limite_inferior:.2f}\nLimite superior: {limite_superior:.2f}') 

pressionar_tecla('E')


# separar numeros que sao outliers dos que nao sao e mostrar o resultado
limpar()
itens_sem_outliers = []
outliers = []

for i in lista_organizada:
    if i >= limite_inferior and i <= limite_superior:
        itens_sem_outliers.append(i)
    else:
        outliers.append(i)    

print("Resultado\n")
print("Lista original:")
imprimir_lista(lista_organizada)

print("\n\nLista sem outliers:")
imprimir_lista(itens_sem_outliers)

print(f"\n\nQuantidade de outliers encontrados: {(len(lista_organizada)) - (len(itens_sem_outliers))}\n")
print("Outliers:")
imprimir_lista(outliers)