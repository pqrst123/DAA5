'''Design n-Queens matrix having first Queen placed. 
Use backtracking to place remaining Queens to generate the final n-queen‘s matrix.'''
# global N
# N = 4
# def printSolution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=" ")
#         print()
# def isSafe(board, row, col):
#     for i in range(col):
#         if board[row][i] == 1:
#             return False
#     for i, j in zip(range(row, -1, -1),
#                     range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#     for i, j in zip(range(row, N, 1),
#                     range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#     return True
# def solveNQUtil(board, col):
#     if col >= N:
#         return True
#     for i in range(N):
#         if isSafe(board, i, col):
#             board[i][col] = 1
#             if solveNQUtil(board, col + 1) == True:
#                 return True
#             board[i][col] = 0
#     return False
# def solveNQ():
#     board = [[0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0]]
#     if solveNQUtil(board, 0) == False:
#         print("Solution does not exist")
#         return False
#     printSolution(board)
#     return True
# solveNQ()


class Solution:
    def solveNQueens(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


def main():
    n = int(input("Enter the value of n for N-Queens: "))
    solution = Solution()
    result = solution.solveNQueens(n)

    print(f"All solutions for {n}-Queens:")
    for board in result:
        for row in board:
            print(row)
        print()


if __name__ == "__main__":
    main()



