faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("faturamento da empresa R$", faturamento)
print(f"Faturamento da empresa: R${faturamento:.2f} custo: R${custo:.2f} lucro: R$ {lucro:.2f}")

email_cliente = " jamilapaim942992@gmail.com "

print (email_cliente)

# Maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)

#Minusculas
email_cliente = email_cliente. lower()
print(email_cliente)

#encontrar o @ ou outro caracteres quaisquer 
print(email_cliente. find ("@"))
