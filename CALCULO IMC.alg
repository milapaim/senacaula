algoritmo "calculoIMC"
// Função :
// Autor :
// Data : 21/11/2024
// Seção de Declarações 
var
   nome: caracter
   imc, peso, altura: Real
inicio
// Seção de Comandos 
   ESCREVAL ("Digite o seu nome: ")
   Leia (nome)
   Escreval ( "Digite o seu peso: ")
   Leia (peso)
   escreval ("Digite a sua altura: ")
   Leia (altura)
   imc<- peso / (altura * altura)
   escreval (" o IMC de " , nome, " é " , imc )

  escreval ("A tabela do IMC " )
  escreval ("resultados menores que 16 — magreza grave; " )
  escreval ("resultados entre 16 e 16,9 — magreza moderada; " )
  escreval ("resultados entre 17 e 18,5 — magreza leve;" )
  escreval ("resultados entre 18,6 e 24,9 — peso ideal; " )
  escreval ("resultados entre 25 e 29,9 — sobrepeso; " )
  escreval ("resultados entre 30 e 34,9 — obesidade grau I;")

fimalgoritmo


