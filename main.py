import sys

from TSP import TSP

t_n_string = input().split(" ", 2)
t = int(t_n_string[0])
n = int(t_n_string[1])
matrix = []
for i in range(n):
    matrix.append([int(mat) for mat in input().split(" ", n)])

result = TSP.find_way(matrix, t)

print(result[1])
output = ""
for i in range(n):
    output += str(result[0][i] + 1) + " "

output += "1"

print(output)
