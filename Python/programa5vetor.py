# Programa para ler um vetor de 5 números inteiros e mostrá-los
def main():
  
    vetor = []
    
    print("Digite 5 números inteiros:")
    
   
    for i in range(5):
        numero = int(input(f"Digite o número {i + 1}: "))
        vetor.append(numero)
    
 
    print("\nOs números digitados foram:")
    for numero in vetor:
        print(numero)

if __name__ == "__main__":
    main()
