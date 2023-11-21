def prnt(lst,strt):
  if strt>=0:
    prnt(lst,strt-1)
    print(lst[strt])
    if strt==len(lst)-1:
      print('Конец списка')
      return
  else:
    return      

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
prnt(my_list,len(my_list)-1)
