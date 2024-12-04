
def maior(*numeros):  # Define a função que aceita múltiplos argumentos
    cont = maior = 0
    print("Analisando os valores passados...")
    
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)  # Mostra os valores
        if cont == 0:  # Define o primeiro valor como maior inicial
            maior = valor
        else:  # Compara os valores subsequentes
            if valor > maior:
                maior = valor
        cont += 1
    
    print(f"\Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.\n")

# Programa principal
print max:() () ()
("Analisando os valores passados...")

