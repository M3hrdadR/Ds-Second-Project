import random


def read_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            # a[i][j] = int(input("Enter the %d row and %d column:" % (i, j)))
            a[i][j] = random.randint(0, 100) % 2
            return a


def max_matrix(a, n, m):
    max_index_i = 0
    max_index_j = 0
    horizontal_edge = 0
    vertical_edge = 0
    max_area = 0
    for row in range(n):
        for col in range(m):
            for ro in range(n - row):
                for co in range(m - col):
                    error = 0
                    tmp = a[ro][co]
                    for r in range(row):
                        for c in range(col):
                            if a[r + ro][c + co] != tmp:
                                error = 1
                                break
                        if error:
                            break
                        if row * col > max_area:
                            max_area = row * col
                            max_index_i = ro
                            max_index_j = co
                            horizontal_edge = row
                            vertical_edge = col
    for i in range(horizontal_edge):
        for j in range(vertical_edge):
            print(a[i + max_index_i][j + max_index_j], end=" ")
        print()


n = int(input("Enter the number of rows matrix:"))
m = int(input("Enter the number of columns matrix:"))
a = [[0 for j in range(n)]for i in range(n)]
a = read_matrix(a)
max_matrix(a)
