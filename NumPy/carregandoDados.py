import numpy as np

#skiprows vai pular a primeira linha, que é o cabeçalho.
#Unpack vai atribuir o valor de cada coluna as variaveis col1,col2,col3
col1, col2, col3 = np.loadtxt('dados.txt', skiprows=1, unpack=True) 

print("Dados coesos:")
print(col1)
print(col2)
print(col3)

#filling_values vai substituir dados string pelo valor passado (so aceita numero)
col1, col2, col3 = np.genfromtxt('dadosFaltantes.txt', skip_header=1, filling_values=0, unpack=True)

print("\nDados Missing:")
print(col1)
print(col2)
print(col3)

