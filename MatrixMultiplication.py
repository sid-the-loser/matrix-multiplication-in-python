"""
Author: Sidharth S

Project subject: Just a simple matrix multiplication function.

Royalty: Nope, don't even need a free shoutout, use it for comertial or indie puposes, I don't mind : )
"""

def MatrixMultiplication(a, b):
    """

    This function can be used for matrix multiplication.

    Please note:

        This function takes two variables a and b respectively.
        It is a simple algorithm, there are no filters implemented to understand which
        matrix is bigger and which one is the small one...look...I know you didn't understand
        what I'm trying to say here, but here are some examples to help you out:

            a = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]

            b = [34, 23, 89]

        The example above will return a list: [34, 23, 0]

        Basically, this function is expecting "a" to be the bigger matrix and "b" to be
        the small matrix.

        If you reverce the "a" and "b" you will get this:

            a = [34, 23, 89]
            
            b = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]

        The result would be an error: "TypeError: object of type 'int' has no len()"
    
    """

    result = []
    
    for a1 in a:

        x = 0
        
        for i in range(len(a1)):
            x += a1[i]*b[i]

        result.append(x)

    return result

# Sorry if there are any spelling errors, if you find any errors in my code, feel free to let me know @sid-loser (twitter) or @sid-the-loser (instagram)
