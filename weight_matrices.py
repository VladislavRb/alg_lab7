from math import inf


weight_matrices_array = [
    [[0, 1, 3, 2],
     [1, 0, 5, 3],
     [3, 5, 0, 7],
     [2, 3, 7, 0]],

    [[0, 9, 9, inf, inf, 8, inf, inf, inf, 18],
     [9, 0, 3, inf, 6, inf, inf, inf, inf, inf],
     [9, 3, 0, 2, 4, 9, inf, inf, inf, inf],
     [inf, inf, 2, 0, 2, 8, 9, inf, inf, inf],
     [inf, 6, 4, 2, 0, inf, 9, inf, inf, inf],
     [8, inf, 9, 8, inf, 0, 7, inf, 9, 10],
     [inf, inf, inf, 9, 9, 7, 0, 4, 5, inf],
     [inf, inf, inf, inf, inf, inf, 4, 0, 1, 4],
     [inf, inf, inf, inf, inf, 9, 5, 1, 0, 3],
     [18, inf, inf, inf, inf, 10, inf, 4, 3, 0]]
]