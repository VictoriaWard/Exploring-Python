# MIT Open Courseware - Introduction to Computer Science and Programming
# Problem Set 1 - Successive Approximation: Polynomials, Derivatives and Newton's Method
# by Victoria Ward

"""
Problem #1
Implement the evaluate_poly function. This function evaluates a
polynomial function for the given x value. It takes in a tuple of
numbers poly and a number x. By number, we mean that x and each
element of poly is a float. evaluate_poly takes the polynomial
represented by poly and computes its value at x. It returns this value
as a float.
"""

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of floats, length > 0
    x: float
    returns: float
    """
    
    poly_value = 0
    for i in poly:
        poly_value += (poly[(poly.index(i))]) * (x ** (poly.index(i)))
    return poly_value



"""
Problem #2
Implement the compute_deriv function. This function computes the
derivative of a polynomial function. It takes in a tuple of numbers
poly and returns the derivative, which is also a polynomial
represented by a tuple.
"""                                       

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """

    deriv = ()
    for i in poly:
        if (poly.index(i)) > 0:
            deriv = deriv + (((poly.index(i)) * i),)
    return deriv



"""
Problem #3
Implement the compute_root function. This function applies Newton’s
method of successive approximation to find a root of the polynomial
function. It ends when it finds a root x such that the absolute value
of f(x) is less than epsilon, i.e. f(x) is close enough to zero. It
returns the root it found as a float.
"""

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    
    xn = x
    i = 1.0
    deriv = compute_deriv(poly)
    
    while abs(evaluate_poly(poly, xn)) > epsilon:
        xn = xn - evaluate_poly(poly, xn) / evaluate_poly(deriv, xn)
        i += 1.0
    return xn, i
