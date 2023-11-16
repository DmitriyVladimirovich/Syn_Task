A=int(input('Введите меньшее число: '))
B=int(input('Введите большее число: '))
if A%2!=0:
  A+=1
for i in range(A,B+1,2):
  print(i,end=' ')
