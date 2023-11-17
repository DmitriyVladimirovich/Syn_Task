def fctrl(a):
  sm=1
  if a<=0:
    return 0
  else:
    for i in range(1,a+1):
      sm*=i
    return sm

l=[]
c=int(input('Введите натуральное число: '))
num=fctrl(c)
for i in range(num,0,-1):
  l+=[fctrl(i)]
print(l)
