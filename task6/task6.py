import numpy as np


def read_csv(csv_file):
    with open(csv_file) as file:
        pre_result = []
        result = []
        my_row = []
        csv_string = file.read()
        csv_string = csv_string.split("\n")

        for row in csv_string:
            pre_result.append(eval(row))

        for i in range(0, len(pre_result[0])):
            for j in range(0, len(pre_result[0])):
                my_row.append(pre_result[j][i])
            result.append(my_row)
            my_row = []

    return result


def build_matrix(matrix):
    arr_matrix = []
    new_row = []

    for k in range(0, len(matrix)):
        for i in range(0, len(matrix[k])):
            for j in range(0, len(matrix[k])):

                if (matrix[k][i] < matrix[k][j]):
                    new_row.append(1)
                elif (matrix[k][i] == matrix[k][j]):
                    new_row.append(0.5)
                elif (matrix[k][i] > matrix[k][j]):
                    new_row.append(0)

        arr_matrix.append(new_row)
        new_row = []

    return arr_matrix


def build_one_matrix(matrixs):
    oneMatrix = []

    for i in range(0, len(matrixs[0])):
        summa = 0

        for k in range(0, len(matrixs)):
            summa += matrixs[k][i]

        oneMatrix.append(summa / len(matrixs))

    return oneMatrix


def split(a, n):
    k, m = divmod(len(a), n)

    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def build_KMatrix(oneMatrix, k=[1 / 3, 1 / 3, 1 / 3]):
    kMatrix = list(split(oneMatrix, len(k)))
    n = len(kMatrix[0])
    kP = np.ones(n) / n
    kN = None

    while True:
        y = np.matmul(kMatrix, kP)
        lbd = np.matmul(np.ones(n), y)
        kN = (1 / lbd) * y
        diff = abs(kN - kP)
        max = diff.max()

        if max <= 0.001:
            break
        else:
            kP = kN

    return np.around(kN, 3)


def task(csvString):
    res1 = read_csv(csvString)
    res2 = build_matrix(res1)
    res3 = build_one_matrix(res2)
    res4 = build_KMatrix(res3)

    return res4


print(task("./task6_data.csv"))