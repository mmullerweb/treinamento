# Faça um programa que peça a nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que informe um valor inválido.
def teste():
    nota = 0
    while(nota >= 0 and nota <= 10):
        nota = int(input("Informe a nota... "))
    print("Nota foi inválida... ")
#teste()
#print(1)

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b
print(soma(1,5))
print(subtracao(9,4))
