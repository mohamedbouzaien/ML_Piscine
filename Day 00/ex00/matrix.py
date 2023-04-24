class Matrix():
    def __init__(self, *arg):
        if (len(arg) != 1):
            raise ValueError("One Matrix argument expected!")
        self.data = arg[0]
        self.shape = len(arg[0]), len(arg[0][0])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise AttributeError("add: left operator isn't a Matrix")
        if self.shape != other.shape:
            raise ValueError("add: different shapes!")
        result = [[self.data[i][j] + other.data[i][j]
                  for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return result

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            raise AttributeError("add: left operator isn't a Matrix")
        if self.shape != other.shape:
            raise ValueError("add: different shapes!")
        result = [[other.data[i][j] + self.data[i][j]
                  for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return result

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise AttributeError("sub: left operator isn't a Matrix")
        if self.shape != other.shape:
            raise ValueError("add: different shapes!")
        result = [[self.data[i][j] - other.data[i][j]
                  for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return result

    def __rsub__(self, other):
        if not isinstance(other, Matrix):
            raise AttributeError("sub: left operator isn't a Matrix")
        if self.shape != other.shape:
            raise ValueError("add: different shapes!")
        result = [[other.data[i][j] - self.data[i][j]
                  for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return result

    def __mul__(self, other):

        result = Matrix(col=other.shape[1], row=self.shape[0])
        for i in range(self.shape()[0]):
            for j in range(other.shape()[1]):
                for k in range(self.shape()[1]):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def __rmul__(self, other):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        line = [self.data[i] for i in range(self.shape[0])]
        return "Matrix(" + str(line) + ")"


class Vector(Matrix):
    def __init__(self) -> None:
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __str__(self, other):
        pass

    def __repr__(self, other):
        pass
