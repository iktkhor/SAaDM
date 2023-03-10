from io import StringIO
import numpy as np
import json

SEQ_LEN = 10


def create_row(visited: set, cur: int) -> np.array:
    row = []

    for i in range(SEQ_LEN):
        row.append(1 if i + 1 in visited else 0)

    return np.array(row)


def create_matrix(data: list) -> np.array:
    visited = set()
    matrix = list()

    for elem in data:

        if type(elem) == str:
            visited.add(int(elem))
            row = create_row(visited=visited, cur=int(elem))
            matrix.append({'num': int(elem), 'row': row})
        else:
            for subelem in elem:
                visited.add(int(subelem))

            for subelem in elem:
                row = create_row(visited=visited, cur=int(subelem))
                matrix.append({'num': int(subelem), 'row': row})

    matrix.sort(key=(lambda x: x['num']))
    raw = [elem['row'] for elem in matrix]

    return np.array(raw)


def find_err(json_path: str) -> list:
    data = json.loads(open(json_path).read())

    matrix1 = create_matrix(data['input1'])
    matrix2 = create_matrix(data['input2'])

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []

    for i in range(criterion.shape[0]):

        for j in range(i):

            if not criterion[i][j]:
                answer.append([j + 1, i + 1])

    flag = True

    for row in data['output']:
        flag *= ([int(row[0]), int(row[1])] in answer)

        if not flag:
            print(f"Ошибка {row}")

    if flag:
        print("Успешно!")

    return answer


def task(str1, str2) -> list:
    str1 = eval(str1)
    str2 = eval(str2)

    matrix1 = create_matrix(str1)
    matrix2 = create_matrix(str2)

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []

    for i in range(criterion.shape[0]):
        for j in range(i):
            if not criterion[i][j]:
                answer.append([str(j + 1), str(i + 1)])

    return answer