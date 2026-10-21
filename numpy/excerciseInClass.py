import numpy as np

a = np.random.randint(1, 200, (10, 8))
newA = a[((a >= 33) & (a <= 66)) | (a >= 190)]
print(a)
print(newA)