from sklearn.datasets import load_iris
from sklearn.preprocessing import normalize

iris=load_iris()
x=iris.data[:10]
print(f'the original data: \n {x}')
y=iris.target
normalize_x=normalize(x,norm='l2')
print(f'the normalized data: \n {normalize_x[:10]}')