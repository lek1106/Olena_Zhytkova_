import numpy as np
matrix=np.arange(1,26,1)
matrix.shape=(5,5)
print(matrix)
column=matrix.sum(axis=1)
matrix_column=np.column_stack((matrix,column))
row=matrix_column.sum(axis=0)
matrix_column_row=np.row_stack((matrix_column,row))
print(matrix_column_row)

