faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("faturamento da empresa R$", faturamento)
print(f"Faturamento da empresa: R${faturamento:.2f} custo: R${custo:.2f} lucro: R$ {lucro:.2f}")

email_cliente = " jamila942992@gmail.com "
print (email_cliente)
# Maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)

#Minusculas
email_cliente = email_cliente. lower()
print(email_cliente)

#encontrar o @ ou outro caracteres quaisquer 
print(email_cliente. find ("@"))

# Tamanho de texto
print( len(( email_cliente)))

#Pegar um caracter
print(email_cliente[7])
print( email_cliente[-4])

#Pegar um pedaço do texto
print( email_cliente[:8])
print( email_cliente[7:])
print( email_cliente[3:10])

# Trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "yahoo.com.br")
print (email_cliente)
print(novo_email)

nome = "josé eduardo soares lima"

print(nome.capitalize())
print (nome.title())
print (nome.upper())

# Pegar o servidor do email
posicao_arroba = email_cliente.find ("@") +1
servidor = email_cliente[posicao_arroba:]
print (servidor)

# Pegar o primeiro nome 
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].title()
print(primeiro_nome)
                                



