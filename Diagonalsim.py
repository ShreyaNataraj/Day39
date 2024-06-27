#brute force approch
# calculates the sum of the primaryDiagonal elements
def diagonal_sum(matrix):
  total =0
  for i in range(len(matrix)):
    total+=matrix[i][i]
  return total
matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(matrix))
#primaryDiagonal i==j
#secondaryDiagonal i+j = n-1 matrix.length-1

#calculates the sum of the both primary Diagonal and secondary Diagonal
def diagonal_sum(matrix):
  total =0
  #PRIMARY DIAGONAL
  for i in range(len(matrix)):
    total+=matrix[i][i]
    #SECONDARY DIAGONAL
    if i != len(matrix)-1-i:
      total+=matrix[i][len(matrix)-i-1]
      
  return total
matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(matrix))