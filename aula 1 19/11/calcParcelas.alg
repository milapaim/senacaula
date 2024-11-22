algoritmo "calParcelas"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   valorEmp, juros, parcelas, rJuros, resposta:Real


inicio
// Seção de Comandos
   escreval("Quanto vou pagar de impréstimo? R$ ")
   Leia(valorEmp)
   escreval()
   escreval("Qual valor dos juros cobrados pelo banco em % ")
   Leia(juros)
   escreval()
   escreval("Quantas parcelas quero dividir para pagar?")
   Leia (parcelas)
   rJuros<- (valorEmp * juros) /100)
   escreval()
   escreval()
   escreval(" o valor dos meus juros será de R$ ", rJuros:5:2)
   resposta<- (rJuros + valorEmp)  /parcelas
   escreval()
   escreval()
   escreval()
   escreval()
   escreval("o valor das ", parcelas,"parcelas que terei que pagar é de R$", resposta:5:2)
fimalgoritmo

