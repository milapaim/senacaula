from sys import intern


ant =  atual = numaux = cont = 0


valor = int (input( "digite o valor para calculo: "))
ant = 0
atual = 1
cont = 1
print (ant)
print(atual)
while (cont < valor):
     numaux = ant + atual
     print(numaux)
     ant = atual
     atual = numaux
     cont = cont +1


