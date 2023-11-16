zeros=0
N=int(input('Введите количество чисел: '))
for i in range(N):
  a=int(input('Введите целое число: '))
  if a==0:
    zeros+=1
print('Нулей:', zeros)
