import random # Escolher aleatoriamente  valores 
import time # controlar tempo de animação

print("Bem-Vindo a maquina de caça níquel insira um valor inicial para começar a apostar:")

deposito = float(input("Faça um depósito para apostar:\n")) # valor depositado

saldo = deposito # saldo inicial

continuar = "S" # variavel de confirmação de loop
while continuar.upper() == "S": # LOOP
     

    valor = float(input("Informe um valor para fazer uma aposta\n"))
    
    saldo -= valor # calcular sando atual subtraindo saldo = depósito menos valor apostado

    print("===================================")

    print(f"Seu depósito foi de R$ {deposito}")
    print(f"Sua aposta foi de R$ {valor}")


    

    print("===================================")

    confirmar = input("Confirma? S/N\n")

    print("===================================")

    if confirmar.upper() == "S" and valor <= saldo: 
    # aposta só ocorre se variavel confirmar = "S" e valor apostado for menor que saldo atual

        emoji = ["🍒","💰","𝟕"] # lista de combinações de aposta

        for i in range(10):
            e1 = random.choice(emoji) # sorteio aleatorio usando random 1
            e2 = random.choice(emoji) # sorteio aleatorio usando random 2
            e3 = random.choice(emoji) # sorteio aleatorio usando random 3
            
            print(e1 , e2 , e3, end="\r") # mostra sorteio mas subscrevendo o conteudo na mesma linha
            
            time.sleep(0.2) # velocidade do sorteio
        print(f"{e1} | {e2} | {e3}") # resultado do sorteio

        if e1 == "🍒" and e2 == "🍒" and e3 == "🍒": # conbinação 1
            valor *= 2
            print(f"Parabéns você ganhou o premio de R${valor}")
            saldo += valor
            print(f"Seu saldo atual é de {saldo}")
            
            
        elif e1 == "💰" and e2 == "💰" and e3 == "💰": # conbinação 2
            valor *= 4
            print(f"Parabéns você ganhou o premio de R${valor}")
            saldo += valor
            print(f"Seu saldo atual é de {saldo}")
        
            
        elif e1 == "𝟕" and e2 == "𝟕" and e3 == "𝟕": # conbinação 3
            valor *= 7
            print(f"MEGA GANHO DE  R${valor}")
            saldo += valor
            print(f"Seu saldo atual é de {saldo}")

        else : # caso nenhuma combinação seja atendida
            print("===================================")
            print(f"Seu saldo é de R${saldo}")
            continuar = input("Deseja tenta novamente S/N? \n")
    
    elif confirmar.upper() == "N": # caso variavel confirma for = "N"
        print("Aposta cancelada")
        exit()
        
    else: # caso saia do loop "confirmação for diferente de "S" e "N" ou caso uma das duas condições para a variavel confirmar não forem atendindas
        print(f"Seu saldo é de R${saldo}")
        print("Erro, resposta não indentificada ou valor da aposta maior que depósito disponivel")