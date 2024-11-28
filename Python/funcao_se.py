# vendas = 1500
# meta = 1300

# # > maior que
# # < menor que 
# # >= maior ou igual a 
# # <= menor ou igual a 
# # == igual a
# # != diferente

# if vendas >= meta:
#  print ("vendedor ganhou Bonus")
#  print ("bateu a meta da vendas")
#  Bonus = 0.1 * vendas
#  print(" bonus do vendedor", Bonus )
# else:
#  print ("vendedor não ganhou Bonus")
#  print ("não Bateu a meta de vendas")

# print("acabou o programa")

# #segundo cenário
# venda = 2500
# meta1 = 1300 # Ganha 10%
# meta = 2000 # Ganha 13%

# if venda >= 2000:
#     bonus = 0.13 * vendas
# else:
#   if vendas >= 1300:
#      bonus = 0.1 * vendas
#   else: 
#      bonus = 0

# print("bonus ", bonus)


# terceiro cenário

vendas = 2500
venda_empresa = 20000
meta_empresa = 10000
meta1 = 1300 # Ganha 10%
meta = 2000 # Ganha 13%

if vendas >= 2000 and venda_empresa >= meta_empresa:
   bonus = 0.13 * vendas
elif vendas >= 13000 and venda_empresa >= meta_empresa:
   bonus = 0.1 * vendas
else:
   bonus = 0 

print ("bonus: ", bonus) 

lista_produtos = ["airpod", "ipad", "iphone", "mackbook"]
produto_procurado = input("procure o produto:")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("produto em estoque.")
else:
   print("nao temos em estoque.") 
      
