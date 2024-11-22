algoritmo "fatorial"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   c, f, n: inteiro
inicio
// Seção de Comandos 
   escreval("digite um número: ",n)
   leia (n)
   se (n = 0)entao
        escreval (1)
   senao
        f <- n
        c <- 1
        enquanto (c < n)faca
                  f <- f*(n-c)
                  c <- c + 1
                  escreval(f)
        fimenquanto

   fimse

fimalgoritmo
