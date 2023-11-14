s=input('Введите слово маленькими латинскими буквами: ')
a=s.count('a')
e=s.count('e')
i=s.count('i')
o=s.count('o')
u=s.count('u')
print('Количество гласных букв в строке: ',a+e+i+o+u)
print('Количество согласных букв в строке: ',len(s)-(a+e+i+o+u))
print('Количество букв:')
if a!=0:
    print('a -',a)
else:
    print('a -',False)
if e!=0:
    print('e -',e)
else:
    print('e -',False)
if i!=0:
    print('i -',i)
else:
    print('i -',False)
if o!=0:
    print('o -',o)
else:
    print('o -',False)
if u!=0:
    print('u -',u)
else:
    print('u -',False)
