x=float(input('Введите минимальную сумму инвестиций: '))
a=float(input('Укажите размер инвестиций Майкла: '))
b=float(input('Укажите размер инвестиций Ивана: '))
if a>=x and b>=x:
  print(2)
elif a>=x and b<x:
  print('Mike')
elif a<x and b>=x:
  print('Ivan')
elif (a+b)>=x:
  print(1)
else:
  print(0)
