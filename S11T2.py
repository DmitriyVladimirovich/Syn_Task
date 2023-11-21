#--
#Структура 0-pets, 1-key, 2-pname, 3-ТТХ
#--

def create(pets):
#    import collections                             #не работает
#    last = collections.deque(pets, maxlen=1)[0]    #не работает
    if len(pets)==0:
        last=0
    else:
        last=[i for i in pets.keys()][-1]+1
#        print('Testcount-',last)
    pet=dict()
    ttx=dict()
    typ=input('Укажите вид питомца: ')
    pname=input('Укажите имя питомца: ')
    age=int(input('Укажите возраст питомца: '))
    mastername=input('Укажите имя хозяина: ')
    ttx['Вид питомца']=typ
    ttx['Возраст питомца']=age
    ttx['Имя хозяина']=mastername
    pet[pname]=ttx
    pets[last]=pet
    return pets
    
def read(pets, key):
# Решение без использования get_pet() - сначала я "выстрадал" его, поэтому оно мне больше нравится
#  pname=[i for i in pets[key].keys()][0]
  pname=[i for i in get_pet(pets,key).keys()][0]
  print('Это', pets[key][pname]['Вид питомца'], 'по кличке', '"'+pname+'".','Возраст:', pets[key][pname]['Возраст питомца'] , get_suffix(pets[key][pname]['Возраст питомца']), 'Имя владельца:', pets[key][pname]['Имя хозяина'])

def get_pet(pets,i):
  return pets[i] if i in pets.keys() else False

def update(pets,key):
    pet=dict()
    ttx=dict()
    typ=input('Измените вид питомца: ')                     #для коммерции можно добавить обработку "enter - не менять значение".
    pname=input('Измените имя питомца: ')
    age=int(input('Измените возраст питомца: '))
    mastername=input('Измените имя хозяина: ')
    ttx['Вид питомца']=typ
    ttx['Возраст питомца']=age
    ttx['Имя хозяина']=mastername
    pet[pname]=ttx
    pets[key]=pet
    return pets

def delete(pets,key):
    if key in pets:
        del pets[key]
        return pets
    else:
        return False

def get_suffix(x):
  teens={11,12,13,14,15,16,17,18,19}
  tails={0,5,6,7,8,9}
  hv=x%10
  if (x in teens) or (hv in tails):
    return 'лет.'
  elif hv==1:
    return 'год.'
  else:
    return 'года.'

def pets_list(pts):
  for i in pts:
    read(pts,i)

pets=dict()
command=input('Введите команду (create, list, update, delete, stop): ')
while command!='stop':
    if command=='create':
        create(pets)
    elif command=='list':
        pets_list(pets)
    elif command=='update':
        a=int(input('Введите цифровой индекс изменяемой записи:'))
        update(pets,a)
    elif command=='delete':
        a=int(input('Введите цифровой индекс изменяемой записи:'))
        delete(pets,a)
    else:
        print('Неверная команда, повторите ввод: ')
    command=input('Введите команду (create, list, update, delete, stop): ')
