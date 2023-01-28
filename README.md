# MatrixMultiplication

Programming assignment for University of Helsinki course Cloud and Edge computing. The main focus in this project is in the benchmarking and evaluation of the solution, not in the code itself.

## How to run it

1. `git clone git@github.com:Melimet/MatrixMultiplication.git` & cd inside the cloned repo
2. Run these commands to enter venv and install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. The script can now be run with `python3 src/main.py`

# P1 - Matrix Multiplication 
*Erkka Rahikainen*

## 1 Availability (0.5 points)

Code for the submission is available in https://github.com/Melimet/MatrixMultiplication.

## 2 Programming Languages and Libraries (0.5 points)

I chose Python and NumPy for this task since with these tools the task can be completed very efficiently and with fewer lines of code.

## 3 Methodology (2 points)

Matrices are created with the help of NumPy's random functionalites. The function that generates the matrices is very simple:
```
def generate_matrix(dimensions) -> list:
  width, height = dimensions
  
  rng = np.random.default_rng()
  
  matrix = rng.random(size=[width, height], dtype=np.float32)

  return matrix

```

The matrices are multiplied with NumPy's [matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) function. The line of code responsible for this is as follows:
```
multiplied_matrix = np.matmul(matrix_a, np.matmul(matrix_b, matrix_c))
```


## 4 Dataset (2 points)

## 5 Evaluation (2 points)

## 6 Discussion (3 points)

I faced issues with running out of memory, since Python's default size for floats is 64 bits. I solved this issue by halving the created float value's bit size down to 32 bits. Computing D was smooth sailing after this change.