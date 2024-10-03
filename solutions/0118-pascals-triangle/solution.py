class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [[1]]
        for _ in range(numRows - 1):
            new_row = [1]

            # use a last row temp value
            last_row = triangle[-1]

            # create a new row value
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle
