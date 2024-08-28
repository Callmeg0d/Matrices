from fractions import Fraction


class MatrixSummationError(Exception):
    def __init__(self, message = "Ошибка сложения, для сложения матриц необходимы матрицы с одинаковым размером."):
        self.message = message
        super().__init__(self.message)


class MatrixDimensionError(Exception):
    def __init__(self, message = "Ошибка произведения, количество столбцов первой матрицы должно быть равно количеству строк во второй матрице"):
        self.message = message
        super().__init__(self.message)


class MatrixDeterminantSizeError(Exception):
    def __init__(self, message = "Программа высчитывает детерминант только для матриц размерностей 2x2 и 3x3"):
        self.message = message
        super().__init__(self.message)

class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def size(self):
        return len(self.data), len(self.data[0])

    def sumMatrices(self, *others):
        summed_data = [[0 for _ in range(len(self.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                summed_data[i][j] += self.data[i][j]
        for other in others:
            if self.size() != other.size():
                raise MatrixSummationError()
            for i in range(len(other.data)):
                for j in range(len(other.data[0])):
                    summed_data[i][j] += other.data[i][j]

        return Matrix(summed_data)

    def multiplyByNumber(self, other):
        multi_matrix = [[0 for _ in range(len(self.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                multi_matrix[i][j] = self.data[i][j] * other
                if multi_matrix[i][j] == -0:
                    multi_matrix[i][j] = 0
                if len(str(multi_matrix[i][j])) > 7:
                    multi_matrix[i][j] = round(multi_matrix[i][j], 3)

        return Matrix(multi_matrix)

    def transposition(self):
        transposed_matrix = [[0] * len(self.data) for _ in range(len(self.data[0]))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                transposed_matrix[j][i] = self.data[i][j]

        return Matrix(transposed_matrix)

    def multiplyMatrices(self, other):
        if len(self.data[0]) != len(other.data):
            raise MatrixDimensionError()
        multi_matrix = [[0 for _ in range(len(other.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    multi_matrix[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(multi_matrix)

    def determinant(self):
        if len(self.data) == 2 and len(self.data[0]) == 2:
            matrix_deter = self.data[0][0] * self.data[1][1] - self.data[1][0] * self.data[0][1]
        elif len(self.data) == 3 and len(self.data[0]) == 3:
            matrix_deter = self.data[0][0] * self.data[1][1] * self.data[2][2] + self.data[0][1] * self.data[1][2] * self.data[2][0] \
                       + self.data[0][2] * self.data[1][0] * self.data[2][1] - self.data[2][0] * self.data[1][1] * self.data[0][2] \
                       - self.data[2][1] * self.data[1][2] * self.data[0][0] - self.data[2][2] * self.data[1][0] * self.data[0][1]
        else:
            raise MatrixDeterminantSizeError()

        return matrix_deter


def input_matrix(rows, cols):
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        while True:
            row = list(map(Fraction, input(f"Строка {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Ошибка: введите ровно {cols} элемента(ов).")
    return matrix


def main():
    print("Выберите действие, которое хотите совершить: \n"
          " 1.Суммирование(сумма нескольких матриц), \n"
          " 2.УмножениеНаЧисло(умножение матрицы на число),\n"
          " 3.Транспонирование(транспонирование матрицы), \n"
          " 4.УмножениеМатриц(умножение двух матриц), \n"
          " 5.Детерминант(вычисление детерминанта для матриц 2x2 и 3x3) \n"
          "Для экономии времени следует использовать порядковые номера действий (например, при умножении матриц введите 4).")

    action = input()

    if action == "1":
        num_matrices = int(input("Введите количество матриц: "))
        if num_matrices > 1:
            matrices = []

            for i in range(num_matrices):
                rows = int(input(f"Введите количество строк для матрицы {i + 1}: "))
                cols = int(input(f"Введите количество столбцов для матрицы {i + 1}: "))
                matrix_data = input_matrix(rows, cols)
                matrices.append(Matrix(matrix_data))

            try:
                sum_matrix = matrices[0].sumMatrices(*matrices[1:])
                print(f"\nСумма всех матриц:\n{sum_matrix}")
            except MatrixSummationError as e:
                print(e)
        else:
            print("Для сложения матриц требуется минимум 2 матрицы")

    elif action == "2":
        matrices = []
        rows = int(input(f"Введите количество строк для матрицы: "))
        cols = int(input(f"Введите количество столбцов для матрицы: "))
        matrix_data = input_matrix(rows, cols)
        matrices.append(Matrix(matrix_data))
        number = input(f"Введите число для умножения на матрицу: ")
        try:
            fraction = Fraction(number)
            result_number = float(fraction)
        except ValueError:
            print("Ошибка: некорректный ввод.")

        result_matrix = matrices[0].multiplyByNumber(result_number)

        print(f"\nРезультат умножения матрицы на число\n{result_matrix}")

    elif action == "3":
        matrices = []
        rows = int(input(f"Введите количество строк для матрицы: "))
        cols = int(input(f"Введите количество столбцов для матрицы: "))
        matrix_data = input_matrix(rows, cols)
        matrices.append(Matrix(matrix_data))

        result_matrix = matrices[0].transposition()

        print(f"\nРезультат транспонирования матрицы\n{result_matrix}")

    elif action == "4":
        num_matrices = 2
        matrices = []

        for i in range(num_matrices):
            rows = int(input(f"Введите количество строк для матрицы {i + 1}: "))
            cols = int(input(f"Введите количество столбцов для матрицы {i + 1}: "))
            matrix_data = input_matrix(rows, cols)
            matrices.append(Matrix(matrix_data))

        result_matrix = matrices[0].multiplyMatrices(*matrices[1:])

        print(f"\nРезультат произведения матриц:\n{result_matrix}")

    elif action == "5":
        matrices = []
        rows = int(input(f"Введите количество строк для матрицы: "))
        cols = int(input(f"Введите количество столбцов для матрицы: "))
        matrix_data = input_matrix(rows, cols)
        matrices.append(Matrix(matrix_data))

        result_matrix = matrices[0].determinant()

        print(f"\nРезультат транспонирования матрицы\n{result_matrix}")


if __name__ == "__main__":
    main()
