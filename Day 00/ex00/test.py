from matrix import Matrix

X = Matrix([[12, 7, 3], [4, 5, 6], [7, 8, 9]])

Y = Matrix([[5, 8, 1], [6, 7, 3], [4, 5, 9]])

Z = X + Y
print(X)
for r in Z:
    print(r)
