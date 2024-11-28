contador =fatorial = numeroRecebido = 0
numeroRecebido = int( input("digite o numero:"))
if (numeroRecebido == 0):
    print(1)
else:
    fatorial = numeroRecebido
    contador = 1
while(contador < numeroRecebido ):
    fatorial = fatorial *(numeroRecebido - contador)
    contador =contador + 1
    print (fatorial)
