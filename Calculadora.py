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
        def soma():
            total = 0
            for i in numeros:
                total += i
            return total

        resultado = soma()
        print(f"A soma entre os numeros é: {resultado}")
        
        
elif Operação == "2" or Operação.upper() == "SUBTRAÇÃO":
    def subtração():
        total1 = numeros[0]
        for i in numeros[1:]:
            total1 -= i
        return total1
    resultado1 = subtração()
    print (f"A subtração dos numeros é: {resultado1}")
    
elif Operação == "3" or Operação.upper() == "MULTIPLICAÇÃO":
    def multiplicação():
        total2 = 1
        for i in numeros:
            total2 *= i
        return total2
    resultado2 = multiplicação()
    print (f"A multiplicação ração dos numeros é: {resultado2}")
    
elif Operação == "4" or Operação.upper() == "DIVISÃO":
    def divisão():
        total3 = numeros[0]
        for i in numeros[1:]:
            total3 /= i
        return total3
    resultado3 = divisão()
    print (f"A divisão dos numeros é: {resultado3}")