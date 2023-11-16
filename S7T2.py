s=input('Введите строку длиной не более 1000 символов: ')
for i in range(len(s)//2):
  s=s.replace('  ',' ')
print(s)
