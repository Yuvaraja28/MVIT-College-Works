import copy

class InverseMatrix:
    def __init__(self):
        self.trace = 0
        self.determinant = 0
        self.sum_diagonals = 0
        self.roots = []
        self.solve_cases = []
        self.a_1 = self.matrix = [[], [], []]
        self.a_2 = None
        self.a_3 = None
        self.a1 = self.matrix[0]
        self.a2 = self.matrix[1]
        self.a3 = self.matrix[2]
        self.I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.NULL = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.GetInput()
        self.Trace()
        self.SumDiagonals()
        self.Determinant()
        self.FindRoots()
        self.SolveCases()
        self.Diagonalize()
    def GetInput(self):
        for x in range(3):
            for y in range(3):
                while True:
                    try:
                        self.matrix[x].append(float(input(f"Enter the Value for A{x+1}{y+1} : ")))
                        break
                    except ValueError: pass
    def isNeg(self, num):
        if num < 0:
            return True
        return False
    def Determinant(self):
        self.determinant += self.a1[0] * ((self.a2[1] * self.a3[2]) - (self.a2[2] * self.a3[1]))
        self.determinant -= self.a1[1] * ((self.a2[0] * self.a3[2]) - (self.a3[0] * self.a2[2]))
        self.determinant += self.a1[2] * ((self.a2[0] * self.a3[1]) - (self.a2[1] * self.a3[0]))
        return self.determinant
    def SumDiagonals(self):
        self.sum_diagonals += ((self.a2[1] * self.a3[2]) - (self.a2[2] * self.a3[1]))
        self.sum_diagonals += ((self.a1[0] * self.a3[2]) - (self.a1[2] * self.a3[0]))
        self.sum_diagonals += ((self.a1[0] * self.a2[1]) - (self.a1[1] * self.a2[0]))
        return self.sum_diagonals
    def Trace(self):
        self.trace = self.a1[0] + self.a2[1] + self.a3[2]
        return self.trace
    def MATAlgebric(self, matrix1, matrix2, mode):
        empty_mat = [[], [], []]
        for index_x, x in enumerate(matrix1):
            for index_y, y in enumerate(x):
                if mode == "add":
                    empty_mat[index_x].append(matrix1[index_x][index_y] + matrix2[index_x][index_y])
                else:
                    empty_mat[index_x].append(matrix1[index_x][index_y] - matrix2[index_x][index_y])
        return empty_mat
    def MATNumberMultiplication(self, number, matrix):
        empty_mat = [[], [], []]
        for index_x, x in enumerate(matrix):
            for index_y, y in enumerate(x):
                empty_mat[index_x].append(number * matrix[index_x][index_y])
        return empty_mat
    def MATMultiplication(self, matrix1, matrix2, round_off=True):
        empty_mat = [[], [], []]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    try: empty_mat[x][y] += matrix1[x][z] * matrix2[z][y]
                    except: empty_mat[x].append(matrix1[x][z] * matrix2[z][y])
        if round_off == True:
            empty_mat = [[round(y) for y in x] for x in empty_mat]
        return empty_mat
    def Transpose(self, matrix):
        transposed = copy.deepcopy(matrix)
        for x in range(3):
            for y in range(3):
                transposed[y][x] = matrix[x][y]
        return transposed
    def MATInverse(self, matrix):
        determinant = 0
        determinant += matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
        determinant -= matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[2][0] * matrix[1][2]))
        determinant += matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
        adj_matrix = [[], [], []]
        adj_matrix[0].append((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])) 
        adj_matrix[0].append( - ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])))
        adj_matrix[0].append((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))        
        adj_matrix[1].append( - ((matrix[0][1] * matrix[2][2]) - (matrix[0][2] * matrix[2][1])))
        adj_matrix[1].append((matrix[0][0] * matrix[2][2]) - (matrix[0][2] * matrix[2][0]))
        adj_matrix[1].append( - ((matrix[0][0] * matrix[2][1]) - (matrix[0][1] * matrix[2][0])))
        adj_matrix[2].append((matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1]))
        adj_matrix[2].append( - ((matrix[0][0] * matrix[1][2]) - (matrix[0][2] * matrix[1][0])))
        adj_matrix[2].append((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
        adj_matrix = [[round(y, 9) for y in x] for x in adj_matrix]
        inverse = self.MATNumberMultiplication(1/determinant, self.Transpose(adj_matrix))
        inverse = [[round(y, 9) for y in x] for x in inverse]
        return inverse
    def FindRoots(self):
        self.roots = []
        x_3 = lambda: 1 - 0
        x_2 = lambda x: (- (self.trace)) - x
        x_1 = lambda x: self.sum_diagonals - x
        x_ = lambda x: (- (self.determinant)) - x
        for take in range(-100, 100):
            first = x_3()
            second = x_2(first * take)
            third = x_1(second * take)
            fourth = x_(third * take)
            if fourth == 0:
                self.roots.append(- take)
        if len(self.roots) <= 2:
            self.roots.extend(((3-len(self.roots)) * [0]))
        return self.roots
    def SolveCases(self):
        self.solve_cases = [copy.deepcopy(self.matrix) for x in range(3)]
        for x in range(3):
            self.solve_cases[x][0][0] -= self.roots[x]
            self.solve_cases[x][1][1] -= self.roots[x]
            self.solve_cases[x][2][2] -= self.roots[x]
        return self.solve_cases
    def Diagonalize(self):
        temp = []
        for mat in self.solve_cases:
            x1 = (mat[0][1] * mat[1][2]) - (mat[0][2] * mat[1][1])
            x2 = - ((mat[0][0] * mat[1][2]) - (mat[1][0] * mat[0][2]))
            x3 = (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])
            if x1 == 0 and x2 == 0 and x3 == 0:
                if x1 == 0:
                    x1 = (mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1])
                if x2 == 0:
                    x2 = - ((mat[1][0] * mat[2][2]) - (mat[2][0] * mat[1][2]))
                if x3 == 0:
                    x3 = (mat[1][0] * mat[2][1]) - (mat[1][1] * mat[2][0])
            append = [x1, x2, x3]
            if 0 not in append:
                if self.isNeg(append[0]) and self.isNeg(append[1]) and self.isNeg(append[2]):
                    for x in range(3):
                        append[x] = - append[x]
                while True:
                    if ((append[0] % 2) == 0) and ((append[1] % 2) == 0) and ((append[2] % 2) == 0):
                        for x in range(3):
                            append[x] = append[x] / 2
                    elif ((append[0] % 3) == 0) and ((append[1] % 3) == 0) and ((append[2] % 3) == 0):
                        for x in range(3):
                            append[x] = append[x] / 3
                    elif ((append[0] % 5) == 0) and ((append[1] % 5) == 0) and ((append[2] % 5) == 0):
                        for x in range(3):
                            append[x] = append[x] / 5
                    else:
                        break
            temp.append(append)
        b_matrix = [[], [], []]
        for x in range(3):
            for y in range(3):
                b_matrix[x].append(temp[y][x])
        try:
            b_matrix_inverse = self.MATInverse(b_matrix)
            diagonalized = self.MATMultiplication(self.MATMultiplication(b_matrix_inverse, self.matrix, round_off=False), b_matrix, round_off=True)
            print(f"Diagonalized = \t|\t{diagonalized[0][0]:.2f}\t{diagonalized[0][1]:.2f}\t{diagonalized[0][2]:.2f}\t|")
            print(f"\t\t|\t{diagonalized[1][0]:.2f}\t{diagonalized[1][1]:.2f}\t{diagonalized[1][2]:.2f}\t|")
            print(f"\t\t|\t{diagonalized[2][0]:.2f}\t{diagonalized[2][1]:.2f}\t{diagonalized[2][2]:.2f}\t|")            
            return diagonalized
        except (ZeroDivisionError, OverflowError, ArithmeticError):
            print("Error Occured while Solving the Given Data's")
print("\n\tProgarm to Diagonalize the Matrix")
print("\tCoded by Yuvaraja.M CSE-B Ist Year")
while True:
    try:
        print("\n")
        matrix = InverseMatrix()
    except KeyboardInterrupt:
        print("\nThanks for using my Program to Find the Inverse of the Matrix\n")
        break