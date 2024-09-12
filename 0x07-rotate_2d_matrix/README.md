## 0x07-rotate_2d_matrix
Here's a README file for your program that includes two files: `0-rotate_2d_matrix.py` and `main.py`.

---

# Rotate 2D Matrix

## Description
This program contains a function to rotate a 2D matrix 90 degrees clockwise. The function is implemented in the `0-rotate_2d_matrix.py` file, and the `main.py` file is used to test the function.

## Files
- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix` function.
- `main.py`: Tests the `rotate_2d_matrix` function.

## Function Prototype
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    
    Parameters:
    matrix (list of list of int): The 2D matrix to rotate.
    
    Returns:
    list of list of int: The rotated 2D matrix.
    """
```

## Usage
### 0-rotate_2d_matrix.py
This file contains the implementation of the `rotate_2d_matrix` function.

```python
def rotate_2d_matrix(matrix):
    n = len(matrix[0])
    matr2 = [[matrix[i][j] for i in range(n - 1, -1, -1)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matr2[i][j]
    return matrix
```

### main.py
This file tests the `rotate_2d_matrix` function.

```python
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

## Example
To run the test, execute the `main.py` file:

```bash
python3 main.py
```

### Expected Output
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Explanation
The `rotate_2d_matrix` function works as follows:
1. **Matrix Size**: Determine the size of the matrix `n`.
2. **Create Rotated Matrix**: Create a new matrix `matr2` by iterating over the original matrix in a way that rotates it 90 degrees clockwise.
3. **Update Original Matrix**: Update the original matrix with the values from the rotated matrix `matr2`.

This approach ensures that the original matrix is rotated in place, and the function returns the rotated matrix.
