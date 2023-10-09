import numpy as np
def factorial(n):
    if n==1 or n==0:
     return 1
  #function body
    return  n*factorial(n-1)


def determinant(matrix):
 n=len(matrix)
 if n==1:
  return matrix[0][0]
 else :
         sign=1
         det=0
         for j in range(n):
          sub_matrix=[]
          for i in range(1,n):
                 sub_row=[]
        
                 for k in range(n):
                  if k!=j:
                   sub_row.append(matrix[i][k])
          sub_matrix.append(sub_row) 
         det+=sign*matrix[0][j]*determinant(sub_matrix)
         sign=-1    
 return det

if __name__=='__main__':
 A=[[1,2,3,4],
    [1,2,5,1],
    [1,5,6,3],
    [1,1,2,1]]
 print(determinant(A))
 print("numpydeterminant:{}".format(determinant(A)) )
 def numpy_determinant(matrix):
    return np.linalg.det(matrix)
 print("numpydeterminant:{}".format(determinant(A)) )git