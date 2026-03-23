# teste de funções #
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def delta(a,b,c):
    return b ** 2 - 4*a*c

def x1 (a,b,c):
    return (-b + math.sqrt(delta(a,b,c))) / (2*a)
                 
def x2 (a,b,c):
    return (-b - math.sqrt(delta(a,b,c))) / (2*a)
                 
print(f"o resultado da formula de baskara é \n x1 = {x1 (a,b,c)} \n x2 = { x2 (a,b,c)}")