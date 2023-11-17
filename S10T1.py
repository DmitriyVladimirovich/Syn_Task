pets=dict()
ttx=dict()
teens={11,12,13,14,15,16,17,18,19} 
tails={0,5,6,7,8,9}
typ=input('Укажите вид питомца: ')
pname=input('Укажите имя питомца: ')
age=int(input('Укажите возраст питомца: '))
mastername=input('Укажите имя хозяина: ')
hv=age%10
if (age in teens) or (hv in tails):
    agetxt='лет.'
elif hv==1:
    agetxt='год.'
else:
    agetxt='года.'
#print(age, agetxt)             #Контроль
ttx['Вид питомца']=typ
ttx['Возраст питомца']=age
ttx['Имя хозяина']=mastername
pets[pname]=ttx
#print(pets)                    #Контроль
print('Это', pets[pname]['Вид питомца'], 'по кличке', '"'+pname+'".','Возраст:', pets[pname]['Возраст питомца'] , agetxt, 'Имя владельца:', pets[pname]['Имя хозяина'])
