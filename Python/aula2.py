faturamento = 1200 # tipo int-> numero inteiro.
custo = 750.32 # Tipo: float -> numero com casas decimais.
lucro = faturamento - custo

margemLucro = lucro/faturamento

print("Faturamento foi de",faturamento)
print("o custo foi de", custo)
print("o lucro foi de", lucro)
print("a margem de lucro foi de ", margemLucro)

mensagem = "o faturamneto da loja foi de tanto"
print(type(mensagem))
print("a variavel faturamento é tipo", type(faturamento))
email = "emailqualquer@gmail.com" # tipo string-> str.
teve_lucro = True # variealvel tipo boolean. 
print(type(teve_lucro)) 

#Mod -> resto da divisão.
print(10 % 3)

tempo_contrato = 360 - 110
tempo_anos = tempo_contrato / 12
tempo_meses = tempo_contrato % 12

print("tempo em anos: ", int(tempo_anos), " anos e ", tempo_meses,"meses.")

media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = "Jamila paim" , 35
print(nome)
print(idade)

nome2, idade2 = "" , 0
print(type(nome2))
print(type(idade2))
estado = True

print("a variavel nome2 é tipo", type(nome2))
print("a variavel é  idade2 é tipo", type(idade2))
print(type(n3))
print(type(estado))
print(type(1+2j))