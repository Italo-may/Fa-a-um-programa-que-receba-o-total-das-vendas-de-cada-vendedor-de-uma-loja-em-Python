#5) Faça um programa que receba o total das vendas de cada vendedor de uma loja e 
#armazene-as em uma lista do Python. Receba também o percentual da comissão a que 
#cada vendedor tem direito e armazene-os em uma lista. Receba os nomes dos 
#vendedores e armazene-os em uma terceira lista. 
#Existem apenas 10 vendedores na loja. Calcule e mostre: 
#- um relatório com os nomes dos vendedores e os valores a receber referentes à 
#comissão; 
#- o total das vendas de tosos os vendedores; 
#- o maior valor a receber e o nome de quem o receberá;
#- o menor valor a receber e o nome de quem o receberá.

vendas = [] # lista para armazenar os valores das vendas
comissoes = [] # lista para armazenar os percentuais da comissão
nomes = [] #  lista para armazenar os nomes dos vendedores

# loop para ler os dados de todos os vendedores
for i in range(10):
    print("Vendedor", i+1)
    nome = str(input("Nome: "))
    nomes.append(nome)
    venda = float(input("Total de vendas: "))
    vendas.append(venda)
    comissao = float(input("Percentual de comissão: "))
    comissoes.append(comissao)   

    total_vendas = sum(vendas)

print("Relatório de comissões:")
for i in range(10):
    print("Vendedor", i+1)
    valor_comissao = vendas[i] * comissoes[i] / 100
    print(nomes[i], ":", valor_comissao)

maior_comissao = 0
nome_maior_comissao = ""
menor_comissao = 10
nome_menor_comissao = ""

for i in range(10):
    valor_comissao = vendas[i] * comissoes[i] / 100
    if valor_comissao > maior_comissao:
        maior_comissao = valor_comissao
        nome_maior_comissao = nomes[i]
    if valor_comissao < menor_comissao:
        menor_comissao = valor_comissao
        nome_menor_comissao = nomes[i]

print("Maior comissão:", nome_maior_comissao, "com", maior_comissao)
print("Menor comissão:", nome_menor_comissao, "com", menor_comissao)
print("Total de vendas:", total_vendas)
