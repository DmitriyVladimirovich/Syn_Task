N=int(input('Введите количество чисел (1<=N<=100000): '))
print(len(set(map(int, input(f'Введите {N} чисел через пробел: ').split(' ')))))
#---
#Здесь можно перед строкой print-а вставить блок на проверку количества введеных чисел взятый из 8 урока задания 2.
#Но я думаю что смысл задания не в копировании уже написанных блоков, а в работе с новыми типами данных.
#Если вы посчитаете иначе - с радостью расширю код и допишу остальные проверки.
#
#s=input(f'Введите {N} чис(ла/ел) через пробел: ')   #сдвоенные пробелы не обрабатываем по условию задачи
#if s[0]==' ':                                       #Убираем пробел в начале
#    s=s.replace(' ','',1)
#if s[-1]==' ':                                      #Убираем пробел в конце
#    s=s[:-1]
#while s.count(' ')!=N-1:                            #считаем сколько чисел ввели и если.. повторяем ввод
#    s=input(f'Вы ввели {s.count(" ")+1} чис(ла/ел). Повторите корректно ввод: ')
#    if s[0]==' ':
#        s=s.replace(' ','',1)
#    if s[-1]==' ':
#        s=s[:-1]
#---