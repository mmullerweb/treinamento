# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# a formula da area de um quadrado (todos os lados sao iguais) A = b * h 

b = input ("Qual a medida da base de um quadrado?" )
h = input ("Qual a medida da altura de um quadrado?" )

area = int (b) * int (h)
dobro = int (area) * 2

print ("O dobro da area de um quadrado e: " + str (dobro))
