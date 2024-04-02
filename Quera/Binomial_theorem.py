def binomial_coefficient(n, k):
    # Calculate the binomial coefficient C(n, k)
    result = 1
    for i in range(1, k + 1):
        result *= (n - i + 1) // i
    return result

def binomial_theorem_expression(n):
    result = ""
    for k in range(n + 1):
        coefficient = binomial_coefficient(n, k)
        term = ""
        if coefficient != 1:
            term += str(coefficient)
        if n - k > 0:
            term += f"x^{n - k}" if n - k > 1 else "x"
        if k > 0:
            term += "" if term else ""
            term += f"y^{k}" if k > 1 else "y"
        if term:
            result += term
            if k < n:
                result += "+"
    return result

# Example usage
n = int(input())
expansion = binomial_theorem_expression(n)
print(expansion)
