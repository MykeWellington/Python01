import numpy as np  

#Criando uma arrey Numpy (vetor)

arr = np.array([1,2,3,4,5])

print(f'Array Numpy:\n {arr}.')

#Operações matematicas em arrays
print('\n Array multiplicado po 2')
print(arr*2)
# Multiplicando posições
print(arr[2]*arr[4])
#operação entre arrays

arr2 = np.array([10,20,30,40,50])

print(arr + arr2)

#Criando uma matriz (2d)

matriz = np.array([[1,2,3],[4,5,6]])
print('\n Matriz de 2x3')
print(matriz)

#Soma e média da matriz
print('\n Soma de todos os elementos da Matriz.')
print(np.sum(matriz))

print('\n Média aritimetica dos elementos da matriz.')
print(np.mean(matriz))

#Transposta de matriz

print('\n Matriz transposta')
print(matriz.T)

#Gerando numeros aleatorios

print('\n Numeros aleatorios entre 0e 1: ')
print(np.random.rand(3,3))

#Valor maximo do array
print('\n Valor máximo da array')
print(np.max(arr2))


# valor minimo do array
print('\n Valor minimo da array')
print(np.min(arr2))

#Desvio padrão em média por dispersão
print ('\n Desvio padrão da array')
print(np.std(arr2))

# indexação avançada
print('\n Elementos maiores que 3')
print(arr[arr > 3])

# Ordenação

arr3 = np.array([18,42,3,1,87,123,74,0])
print ('\n array ordenada')
print(np.sort(arr3))

#Gerando numeros aleatorios entr 1 e 100
print('\n Numeros inteiros entre 1 e 100')
print(np.random.randint(1,100, size=(3,3)))

#Reorganizar os dados
print('\n Reshape da matriz 2x3 para 3x2 ')
print(matriz.reshape(3,2))