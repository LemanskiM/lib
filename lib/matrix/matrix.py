class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])

    def row(self, index):
      """
      index - row index
      return list from picked row
      """
      return self.matrix[index]

    def column(self, column):
      """
      return column in row
      column - index of column to return
      """
      l = []
      for row in self.matrix:
        l.append(row[column])
      return l

x = """ 3 4 5
3 3 4
2 3 4 """

m = Matrix(x)
