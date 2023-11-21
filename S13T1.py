def mx_gen(s,v,k=0):
  import random
  if k=='r':
    return [[random.randrange(-200,200,1) for i in range(s)] for j in range(v)]
  else:
    return [[k for i in range(s)] for j in range(v)]

a=int(input('Укажите размерность матрицы по-горизонтали: '))
b=int(input('Укажите размерность матрицы по-вертикали: '))

matrix_1=mx_gen(a,b,'r') 
matrix_2=mx_gen(a,b,'r')
matrix_3=mx_gen(a,b,0)

for i in range(b):
    for j in range(a):
        matrix_3[i][j]=matrix_1[i][j]+matrix_2[i][j]
print(matrix_1)
print(matrix_2)
print(matrix_3)
