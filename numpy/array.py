import numpy as np

x = np.array([[1,2,3,6],[4,5,6,6],[7,8,9,6],[10,12,12,6]])
print(x)
'''
Imprime los valores en columna si usas la forma [n:m,n:m]
[[6]
 [6]
 [6]
 [6]]
osea de n hasta m, en caso sontrario si solo usas [n:m,n] o [n, n:m]
imprime como un vector o [1 2 3 4]
'''

print(x[1,:])
print(x[:,1:2])
print(x[:,1:2])
print(x[:,-1:None])
print(x[1:3,1:3])
print(x[(x % 2 != 0) | (x > 5)])