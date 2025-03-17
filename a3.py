def multiply_one_iteration(n, m):
    return n * m

def multiply_n_iterations(n, m):
    result = 0
    for _ in range(abs(n)):
        result += m
    # If n is negative, make the result negative
    if n < 0:
        result = -result
    return result

# Example usage:
N = 5
M = 3

# One iteration
result_one = multiply_one_iteration(N, M)
print(f"Multiplying {N} and {M} using one iteration: {result_one}")

# N iterations
result_n = multiply_n_iterations(N, M)
print(f"Multiplying {N} and {M} using N iterations: {result_n}")
