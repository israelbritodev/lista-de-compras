# Escreva um programa em Python que simule uma lista de compras. O usuário deve poder digitar itens livremente, um por vez, e o programa deve armazená-los em uma lista. A entrada termina quando o usuário digitar a palavra "fim" (caso-insensitivo). Ao final, exiba todos os itens da lista em ordem alfabética crescente.

# ** Input ** 
# A entrada será:
#       *** item -> string *** 
# Se item receber o valor de 'fim', encerrar o código.
# Obs.: um item pode ser recebido mais de uma vez. Por exemplo, eu posso receber 'abacaxi' mais de uma vez na variável item

# ** Output **
# A saída deverá exibir cada um dos itens da lista de compras, organizados em ordem alfabética crescente, linha a linha.

lista_de_compras = []
item = str([])

while item.lower() != "fim":
    item = str(input("Digite um item para adicionar à lista de compras (ou 'fim' para encerrar): "))
    if item.lower() != "fim":
        lista_de_compras.append(item)
        
lista_de_compras.sort()

for item in lista_de_compras:
    print(item)