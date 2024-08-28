import pytest
from fractions import Fraction
from project_matrices.matrices import Matrix
from project_matrices.matrices import MatrixSummationError
from project_matrices.matrices import MatrixDimensionError
from project_matrices.matrices import MatrixDeterminantSizeError


def test_sum_two_matrices():
    m1 = Matrix([[1, 2], [3, -4]])
    m2 = Matrix([[-5, 6], [7, 8]])
    result = m1.sumMatrices(m2)
    expected = [[-4, 8], [10, 4]]
    assert result.data == expected


def test_sum_multiple_matrices():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = Matrix([[9, 10], [11, 12]])
    result = m1.sumMatrices(m2, m3)
    expected = [[15, 18], [21, 24]]
    assert result.data == expected


def test_sum_matrices_with_different_sizes():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6, 7], [8, 9, 10]])
    with pytest.raises(MatrixSummationError):
        m1.sumMatrices(m2)


def test_sum_empty_matrix():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[0, 0], [0, 0]])
    result = m1.sumMatrices(m2)
    expected = [[1, 2], [3, 4]]
    assert result.data == expected


def test_sum_multiple_matrices_with_decimals():
    m1 = Matrix([[Fraction("-4/3"), Fraction("0")], [Fraction("18/7"), Fraction("17/2")]])
    m2 = Matrix([[Fraction("9/7"), Fraction("-6")], [Fraction("4/5"), Fraction("-8")]])
    m3 = Matrix([[Fraction("9"), Fraction("-10")], [Fraction("13/8"), Fraction("12")]])

    result = m1.sumMatrices(m2, m3)
    expected = [[Fraction("188/21"), Fraction("-16")], [Fraction("1399/280"), Fraction("25/2")]]
    assert result.data == expected

def test_multi_by_number_integer():
    m1 = Matrix([[Fraction("-4/3"), Fraction("0")], [Fraction("18/7"), Fraction("17/2")], [Fraction("-6"), Fraction("4")]])
    number = 7

    result = m1.multiplyByNumber(number)
    expected = [[Fraction("-28/3"), Fraction("0")], [Fraction("18"), Fraction("119/2")], [Fraction("-42"), Fraction("28")]]
    assert result.data == expected


def test_multi_by_number_float():
    m1 = Matrix([[Fraction("-11/4"), Fraction("0")], [Fraction("0.78"), Fraction("17/9")], [Fraction("-6"), Fraction("1.155")]])
    number = -7.569

    result = m1.multiplyByNumber(number)
    expected = [[20.815, 0], [-5.904, -14.297], [45.414, -8.742]]
    assert result.data == expected


def test_multi_by_number_fractions():
    m1 = Matrix([[Fraction("-13/4"), Fraction("0")], [Fraction("0.78"), Fraction("17/9")], [Fraction("-6"), Fraction("3.1415")]])
    number = 23/13

    result = m1.multiplyByNumber(number)
    expected = [[-5.75, 0], [1.38, 3.342], [-10.615, 5.558]]
    assert result.data == expected


def test_multi_by_number_invalid_number():
    try:
        m1 = Matrix([[Fraction("-13/4"), Fraction("0")], [Fraction("0.78"), Fraction("17/9")], [Fraction("-6"), Fraction("3.1415")]])
        number = "qwe"
        result = m1.multiplyByNumber(number)

    except TypeError as e:
        print(f"Обнаружена ошибка: {e}")

test_multi_by_number_invalid_number()


def test_matrix_transposition():
    m1 = Matrix([[Fraction("-13/4"), Fraction("0")], [Fraction("0.78"), Fraction("17/9")], [Fraction("-6"), Fraction("3.1415")]])
    result = m1.transposition()
    expected = [[Fraction("-13/4"), Fraction("0.78"), Fraction("-6")], [Fraction("0"), Fraction("17/9"), Fraction("3.1415")]]

    assert result.data == expected


def test_matrix_transposition_without_changes():
    m1 = Matrix([[Fraction("1"), Fraction("2"), Fraction("3")], [Fraction("2"), Fraction("6"), Fraction("-8")],
                 [Fraction("3"), Fraction("-8"), Fraction("-7/4")]])
    result = m1.transposition()
    expected = [[Fraction("1"), Fraction("2"), Fraction("3")], [Fraction("2"), Fraction("6"), Fraction("-8")],
                [Fraction("3"), Fraction("-8"), Fraction("-7/4")]]

    assert result.data == expected


def test_multiply_matrices_same_size():
    m1 = Matrix([[1, 2], [3, -4]])
    m2 = Matrix([[-5, 6], [7, 8]])

    result = m1.multiplyMatrices(m2)
    expected = [[9, 22], [-43, -14]]

    assert result.data == expected


def test_multiply_matrices_different_size():
    m1 = Matrix([[Fraction("1"), Fraction("-22/19"), Fraction("4")], [Fraction("3"), Fraction("-4"), Fraction("5")],
                 [Fraction("15/8"), Fraction("0"), Fraction("16")]])
    m2 = Matrix([[Fraction("-5")], [Fraction("4")], [Fraction("-7/3")]])

    result = m1.multiplyMatrices(m2)
    expected = [[Fraction("-1081/57")], [Fraction("-128/3")], [Fraction("-1121/24")]]

    assert result.data == expected


def test_multiply_matrices_different_size_2():
    m1 = Matrix([[Fraction("4"), Fraction("-22/19"), Fraction("0")]])
    m2 = Matrix([[Fraction("5"), Fraction("4"), Fraction("3"), Fraction("-7/3")],
                 [Fraction("-8/7"), Fraction("-4/3"), Fraction("21"), Fraction("0.85")],
                 [Fraction("0"), Fraction("11"), Fraction("3/7"), Fraction("0.99")]])

    result = m1.multiplyMatrices(m2)
    expected = [[Fraction("2836/133"), Fraction("1000/57"), Fraction("-234/19"), Fraction("-5881/570")]]

    assert result.data == expected


def test_multiply_matrices_invalid_sizes():
    m1 = Matrix([[Fraction("9"), Fraction("-44"), Fraction("-6")]])
    m2 = Matrix([[Fraction("1"), Fraction("-2"), Fraction("3"), Fraction("4")],
                 [Fraction("-5"), Fraction("6"), Fraction("-7"), Fraction("8")]])

    with pytest.raises(MatrixDimensionError):
        m1.multiplyMatrices(m2)

def test_determinate_matrix():
    m1 = Matrix([[Fraction("9"), Fraction("8"), Fraction("7")], [Fraction("6"), Fraction("5"), Fraction("4")],
                 [Fraction("3"), Fraction("2"), Fraction("1")]])

    result = m1.determinant()
    expected = 0

    assert result == expected

def test_determinate_matrix_fractions():
    m1 = Matrix([[Fraction("-7/9"), Fraction("9/7")], [Fraction("0"), Fraction("4")]])

    result = m1.determinant()
    expected = Fraction("-28/9")

    assert result == expected

def test_determinate_matrix_size_error():
    m1 = Matrix([[Fraction("-11"), Fraction("21"), Fraction("-31"), Fraction("41")],
                 [Fraction("51"), Fraction("-61")]])

    with pytest.raises(MatrixDeterminantSizeError):
        m1.determinant()

def test_matrices_invalid_elems():
    try:
        m1 = Matrix([[Fraction("1"), Fraction("abcd")], [Fraction("[1, 2, 3]"), Fraction("4")]])
        m2 = Matrix([[Fraction("9/7"), Fraction("8")], [Fraction("4/5"), Fraction("efg")]])

    except ValueError as e:
        print(f"Обнаружена ошибка: {e}")


test_matrices_invalid_elems()


if __name__ == "__main__":
    pytest.main()
