algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 22/11/2024
// Se��o de Declara��es 
var
   ant, atual, numAux, cont, valor: inteiro
   
inicio
// Se��o de Comandos 
   Escreval("digite m valor para calculo:", valor)
   Leia (valor)
   ant<- 0
   Atual <- 1
   Cont <- 1
   Escreval(ant)
   escreval(Atual)
   enquanto cont < valor faca
            numAux <- ant + atual
            escreval (numAux)
            ant <- atual
            atual <- numAux
            cont <- cont +1
   fimenquanto


fimalgoritmo
