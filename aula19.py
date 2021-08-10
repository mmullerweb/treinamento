# Faça um programa que peça a nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que informe um valor inválido.

nota = 0
while (nota >= 0 and nota <= 10):
    nota = int (input("Informe a nota... "))
print ("Nota nao valida ")