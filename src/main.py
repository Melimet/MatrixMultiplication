import numpy as np

def generate_matrix(dimensions) -> list:
  width, height = dimensions
  
  rng = np.random.default_rng()
  
  matrix = rng.random(size=[width, height], dtype=np.float32)
  print(f"Matrix with shape {width}x{height} generated")

  return matrix

def main():
  matrix_shapes = [[10**6, 10**3], [10**3, 10**6], [10**6, 1]]
  #matrix_shapes = [[5,5], [5,5], [5,5]]
  print("Generating matrixes...")
  matrices = list(map(generate_matrix, [(matrix_dimension[0], matrix_dimension[1]) for matrix_dimension in matrix_shapes]))

  print("Multiplying matrix...") 

  matrix_a, matrix_b , matrix_c = matrices

  multiplied_matrix = np.matmul(matrix_a, np.matmul(matrix_b, matrix_c))
  print("Final product shape: ", multiplied_matrix.shape)
  print("Multiplied matrix: ", multiplied_matrix)

main()