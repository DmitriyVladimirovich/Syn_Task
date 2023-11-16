l=lnew=[]
N=int(input('Введите размер массива: '))
for i in range(N):
  l+=[int(input('Введите число: '))]
lnew=l[::-1]
#print(f'Перевернутый массив {lnew}') #Можно так, но задание подразумевает использование цикла...
for i in range(len(lnew)):
  print(lnew[i], end=' ')
