# Задание 1
class WakeUpNeo:
    def __init__(self, matrix_list):
        self.matrix_list = list(matrix_list)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_list]))

    def __add__(self, other):
        sum_matrix = []
        for i in zip(self.matrix_list, other.matrix_list):
            sum_matrix.append([sum([j, k]) for j, k in zip(*i)])
        return WakeUpNeo(sum_matrix)


wun1 = WakeUpNeo([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
wun2 = WakeUpNeo([[31, 22, 5], [37, 43, -7], [51, 86, 1]])
print(wun1)
print(wun2)
print(wun1 + wun2)