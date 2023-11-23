class Kassa:
  def __init__(self,value):
    self.value=value

  def top_up(self,x):
    self.value+=x
#    print('Добавлено:', x,'итого:',self.value)
    return f'Добавлено: {x}, итого: {self.value} тугриков'
  def count_1000(self):
    return f'Целых тысяч: {self.value//1000}'

  def take_away(self,x):
    if self.value>=x:
      self.value-=x
      return f'Вычли {x}, осталось: {self.value}'
    else:
      return 'Error, мало денег'

bank=Kassa(2327711)
print(bank.value)
print(bank.top_up(89))
print(bank.count_1000())
print(bank.take_away(800))
