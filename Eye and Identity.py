import numpy
numpy.set_printoptions(sign=' ')

n, m = map(int, input().split())
print(numpy.eye(n, m, k=0))
