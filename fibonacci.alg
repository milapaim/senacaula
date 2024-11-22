algoritmo "semnome"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   ant, atual, numAux, cont, valor: inteiro
   
inicio
// Seção de Comandos 
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
