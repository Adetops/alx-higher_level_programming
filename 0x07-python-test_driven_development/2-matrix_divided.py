#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    err_mess = "matrix must be a matrix (list of lists) of integers/floats"
    
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(err_mess)
    	for j in matrix[i]:
            if not isinstance(j, int) and not isinstance(j, float):
	    		raise TypeError(err_mess)
			else
				new = "{.2f}".format(j / div)
				new_matrix.append(new)
    
    
    return new_matrix