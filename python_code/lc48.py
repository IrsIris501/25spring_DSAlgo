class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        n=len(matrix)

        temp=deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j]=temp[n-1-j][i]
