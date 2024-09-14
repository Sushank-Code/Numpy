import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)               # base returns the none if array owns it data { copy owns the data}
print(y.base)               