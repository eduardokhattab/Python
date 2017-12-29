"""
arquivo = open('arquivo.txt', 'w') #read write a-arquivo+atualizacao b-binario +atualização

arquivo.write('machines')
arquivo.write('aprende python')

arquivo.close()

arquivo = open('arquivo.txt', 'a') #texto + atualizacao

arquivo.write("\n\n\lololo")

arquivo.close()


texto = '''Tres aspas simples
significam que o texto ocupa mais de uma
linha'''

with open('arquivo.txt', 'a') as f:
    f.write(texto)
"""

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)