# GaussJordan
Gauss-Jordan Elimination Calculator: This is a Python function which uses Gauss-Jordan elimination method to solve a system of a set of linear equations.

## Usage
gauss_jordan(x, y, verbose)

## x
x is a numpy matrix which includes the coefficients

## y
y is a numpy vector which includes the results of the linear equations

## verbose
verbose is the detail level of the output messages.
Default value is 0, which means no output.
verbose = 1 shows a brief output.
verbose = 2 shows all steps of the solution.

## Example
2x + y + z = 8
x + y - 2z = -2
x + 2y + z = 2

x = numpy.array([[2, 1, 1], [1, 1, -2], [1, 2, 1]])
y = numpy.array([8, -2, 2])

b = gauss_jordan(x, y)

Output will be b = [ 4. -2.  2.], which means x=4, y=-2, z=2.
