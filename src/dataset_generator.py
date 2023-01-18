import numpy as np

def generate_matrix(width: int, depth: int) -> list:

  matrix = np.random.uniform(0, 1, size=(width, depth))

  return matrix

def generator():
  
  matrix_a = generate_matrix(10**6, 10**3)
  print(matrix_a)
  matrix_b = generate_matrix(10**3, 10**6) 
  print(matrix_b)
  matrix_c = generate_matrix(10**6, 1)
  print(matrix_c)


generator()