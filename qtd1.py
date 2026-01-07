import baseLoja

lista_vendas = baseLoja.vendas ["vendas"]


print("Lista de vendas: ")
print("ID|PRODUTO|CATEGORIA|QUANTIDADE|VALOR UNITARIO")
for venda in lista_vendas:
    print(f"{venda["id"]} |{venda["produto"]} | {venda["categoria"]} | {venda["quantidade"]} | {venda["valor_unitario"]}")
   
      
total_vendas = 0
media_vendas = 0

for venda in lista_vendas:
    total_vendas += venda["quantidade"] * venda["valor_unitario"]
    
media_geral = total_vendas / len(lista_vendas)
print(f"Total vendas: R${total_vendas:.2f}")
print(f"Média geral: R${media_geral:.2f}")