from operacoes import *



numeros = []

while True:
    numero = input("Digite números (ou OK para parar): ")
    
    print(f"Você digitou: [{numero}]") 
    
    if numero.upper() == "OK":
        break
    
    numeros.append(int(numero))

print("===========================================")

print(f"Numeros fornecidos{numeros}")

print("Escolha qual operação fazer:\n 1.SOMA \n 2.SUBTRAÇÃO \n 3.MULTIPLICAÇÃO \n 4.DIVISÃO")

print("===========================================")

Operação = input()

if Operação == "1" or Operação.upper() == "SOMA":
    resultado = soma(numeros)
    print(f"A soma entre os numeros é: {resultado}")
        
        
        
elif Operação == "2" or Operação.upper() == "SUBTRAÇÃO":
    resultado1 = subtração(numeros)
    print (f"A subtração dos numeros é: {resultado1}")
    

elif Operação == "3" or Operação.upper() == "MULTIPLICAÇÃO":
    resultado2 = multiplicação(numeros)
    print (f"A multiplicação ração dos numeros é: {resultado2}")
    
elif Operação == "4" or Operação.upper() == "DIVISÃO":
    resultado3 = divisão(numeros)
    print (f"A divisão dos numeros é: {resultado3}")