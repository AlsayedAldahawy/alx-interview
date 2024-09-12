# 0x02-minimum_operations
---

# Minimum Operations to Achieve n 'H' Characters

## Problem Description
Given a text file containing a single character 'H', you can perform only two operations:
1. **Copy All**: Copy all the characters present in the file.
2. **Paste**: Paste the copied characters.

Your task is to write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

### Prototype
```python
def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve exactly n 'H' characters.
    
    Parameters:
    n (int): The target number of 'H' characters.
    
    Returns:
    int: The minimum number of operations needed, or 0 if n is impossible to achieve.
    """
```

### Example
```python
n = 9
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6
```

## Explanation
The key to solving this problem is understanding that we cannot achieve any number of 'H' characters by repeating operations other than its prime factors. Therefore, we should be cautious with using the "Copy All" operation to ensure we don't end up with a number that can't reach the desired `n` by repetition.

### Detailed Explanation
1. **Prime Factorization**: The minimum number of operations required to achieve `n` 'H' characters is related to the prime factors of `n`. By breaking down `n` into its prime factors, we can determine the optimal sequence of "Copy All" and "Paste" operations.
2. **Operations Strategy**:
   - For each prime factor, perform a "Copy All" followed by the necessary number of "Paste" operations to multiply the current number of 'H' characters.
   - Sum the prime factors to get the total number of operations.

### Example
For `n = 26`:
- **Prime Factorization**: \( 26 = 2 \times 13 \)
- **Operations**:
  - Start with 1 'H'.
  - Copy All (1 operation), Paste (1 operation) → 2 'H's.
  - Paste 12 more times (12 operations) → 26 'H's.
  - Total operations: \( 1 + 1 + 12 = 14 \).

### Incorrect Strategy
If you use "Copy All" too early, you might get stuck:
- Start with 1 'H'.
- Copy All (1 operation), Paste (1 operation) → 2 'H's.
- Copy All (1 operation), Paste (1 operation) → 4 'H's.
- Now, you can't achieve 26 by repeating 4.

## Implementation
Here's the implementation of the `minOperations` function:

```python
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    if n > 1:
        operations += n
    
    return operations

# Example usage
n = 9
print(f"Min number of operations to reach {n} characters: {minOperations(n)}")
```

## Conclusion
By understanding the relationship between the number of 'H' characters and their prime factors, we can efficiently determine the minimum number of operations needed to achieve exactly `n` 'H' characters in the file.

---
