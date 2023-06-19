class InverseMatrix:
    def __init__(self):
        self.trace = 0
        self.determinant = 0
        self.sum_diagonals = 0
        self.a_1 = self.matrix = [[], [], []]
        self.a_2 = None
        self.a_3 = None
        self.a_inv = None
        self.a1 = self.matrix[0]
        self.a2 = self.matrix[1]
        self.a3 = self.matrix[2]
        self.I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.NULL = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.GetInput()
        self.Trace()
        self.SumDiagonals()
        self.Determinant()
    def GetInput(self):
        for x in range(3):
            for y in range(3):
                while True:
                    try:
                        self.matrix[x].append(float(input(f"Enter the Value for A{x+1}{y+1} : ")))
                        break
                    except ValueError: pass
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
    def MATMultiplication(self, matrix1, matrix2):
        empty_mat = [[], [], []]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    try: empty_mat[x][y] += matrix1[x][z] * matrix2[z][y]
                    except: empty_mat[x].append(matrix1[x][z] * matrix2[z][y])
        return empty_mat
    def Verify(self):
        self.a_2 = self.MATMultiplication(self.matrix, self.matrix)
        self.a_3 = self.MATMultiplication(self.a_2, self.matrix)
        if (self.MATAlgebric(self.MATAlgebric(self.MATAlgebric(self.a_3, self.MATNumberMultiplication(self.trace, self.a_2), "sub"), self.MATNumberMultiplication(self.sum_diagonals, self.a_1), "add"), self.MATNumberMultiplication(self.determinant, self.I), "sub")) == self.NULL:
            return True
        else:
            return False
    def Solve(self):
        if self.Verify():
            try:
                self.a_inv = self.MATNumberMultiplication(1/self.determinant, self.MATAlgebric(self.MATAlgebric(self.a_2, self.MATNumberMultiplication(self.trace, self.a_1), "sub"), self.MATNumberMultiplication(self.sum_diagonals, self.I), "add"))
                self.a_inv_raw = self.MATAlgebric(self.MATAlgebric(self.a_2, self.MATNumberMultiplication(self.trace, self.a_1), "sub"), self.MATNumberMultiplication(self.sum_diagonals, self.I), "add")
                print(f"\nInverse = 1/{self.determinant} \n\t\t|\t{self.a_inv_raw[0][0]}\t{self.a_inv_raw[0][1]}\t{self.a_inv_raw[0][2]}\t|")
                print(f"\t\t|\t{self.a_inv_raw[1][0]}\t{self.a_inv_raw[1][1]}\t{self.a_inv_raw[1][2]}\t|")
                print(f"\t\t|\t{self.a_inv_raw[2][0]}\t{self.a_inv_raw[2][1]}\t{self.a_inv_raw[2][2]}\t|\n")
                print(f"Inverse = \t|\t{self.a_inv[0][0]:.2f}\t{self.a_inv[0][1]:.2f}\t{self.a_inv[0][2]:.2f}\t|")
                print(f"\t\t|\t{self.a_inv[1][0]:.2f}\t{self.a_inv[1][1]:.2f}\t{self.a_inv[1][2]:.2f}\t|")
                print(f"\t\t|\t{self.a_inv[2][0]:.2f}\t{self.a_inv[2][1]:.2f}\t{self.a_inv[2][2]:.2f}\t|")            
            except (ZeroDivisionError, OverflowError, ArithmeticError):
                print("Error Occured while Solving the Given Data's")
        else:
            print("Cayley-Hamilton Theorem Failed to Verify the Zeros")

print("\n\tProgarm to Find the Inverse of a Matrix")
print("\tCoded by Yuvaraja.M CSE-B Ist Year")
while True:
    try:
        print("\n")
        matrix = InverseMatrix()
        matrix.Solve()
    except KeyboardInterrupt:
        print("\nThanks for using my Program to Find the Inverse of the Matrix\n")
        break