class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)
        diagonals = {}

        # Gom các phần tử theo đường chéo (i - j cố định)
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])

        # Sắp xếp từng đường chéo
        for key, vals in diagonals.items():
            if key >= 0:  # tam giác dưới + đường chéo chính
                diagonals[key] = sorted(vals, reverse=True)
            else:         # tam giác trên
                diagonals[key] = sorted(vals)

        # Gán ngược lại
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diagonals[key].pop(0)

        return grid
