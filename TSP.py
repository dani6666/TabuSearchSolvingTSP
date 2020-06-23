import random
import time


class TSP:

    @staticmethod
    def find_way(matrix, time_to_run):
        TSP.tabu_size = len(matrix) ** 2
        deadline = time.time() + time_to_run
        n = len(matrix)
        permutation = [0] + random.sample(range(1, n), n - 1)
        best = permutation
        tabu_list = [permutation]
        while time.time() < deadline:
            neighbours = list(TSP.get_neighbours(permutation))
            best_neighbour = neighbours[0]
            for perm in neighbours:
                if perm not in tabu_list and \
                        TSP.calculate_route(perm, n, matrix) < TSP.calculate_route(best_neighbour, n, matrix):
                    best_neighbour = perm

            permutation = best_neighbour
            tabu_list.append(best_neighbour)
            if TSP.calculate_route(best, n, matrix) > TSP.calculate_route(best_neighbour, n, matrix):
                best = best_neighbour

            if len(tabu_list) == TSP.tabu_size:
                tabu_list.__delitem__(0)

        return best, TSP.calculate_route(best, n, matrix)

    @staticmethod
    def get_neighbours(permutation):
        for i in range(1, len(permutation) - 1):
            result = []
            j = 0
            while j < len(permutation):
                if i == j:
                    result += [permutation[j + 1], permutation[j]]
                    j += 2

                if j < len(permutation):
                    result.append(permutation[j])
                j += 1
            yield result

    @staticmethod
    def calculate_route(permutation, n, matrix):
        result = 0
        for i in range(1, n):
            result += matrix[permutation[i - 1]][permutation[i]]

        result += matrix[permutation[n - 1]][0]

        return result
