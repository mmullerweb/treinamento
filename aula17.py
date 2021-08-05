# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input ("Digite sexo F ou M: ")

if str (sexo) == ("F"): 
    print ("Feminino") 

elif str (sexo) == ("M"): 
    print ("Masculino")

else:
    print ("Sexo invalido")
