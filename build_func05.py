def main(n, x):
    """Integer type variables 'n' and 'x' are given. Return the value of the expression in README.md file.


    Args:
        n (int): integer
        x (int): integer
        
    Returns:
        int: the value of the expression
    """
    return int(n*(n*100))+((n*n)+(x*x))
print(main(3,6))