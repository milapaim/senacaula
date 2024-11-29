ant = atual = numAux = cont = 0
ant = 0
atual= 1
cont =1
print(ant)
print(atual)

valor = int (input( "digite um numero:" ))
while (cont < valor):
    numAux = ant + atual
    print(numAux)
    ant = atual
    atual = numAux
    cont = cont +1
    

    
