class trtl:
  def __init__(self,x=0,y=0,s=1):         #Считаем игровое поле полностью в I четверти коордиатной плоскости
    self.x=x                              #Левый нижний угол - клетка с координатами (0,0)
    self.y=y
    self.s=s

  def go_up(self):
    self.y+=s
  
  def go_down(self):
    self.y-=s

  def go_left(self):
    self.x-=s

  def go_right(self):
    self.x+=s

  def evolve(self):
    self.s+=1

  def degrade(self):
    if self.s>1:
      self.s-=1
    else:
      print('Error нельзя больше уменьшать!')

  def count_moves(self,x1,y1):
    if x1%self.s!=0 and y1%self.s!=0:
      print('Введенные числа должны быть кратны',self.s,'Повторите ввод')
    else:
      dx=(x1-self.x)//self.s
      dy=(y1-self.y)//self.s
      if dx<0:
        tdx='влево'
      elif dx==0:
        tdx='не смещаемся'
      else:
        tdx='вправо'
      if dy<0:
        tdy='вниз'
      elif dy==0:
        tdy='не смещаемся'
      else:
        tdy='вверх'
      if dx!=0 and dy!=0:
        print('По горизонтали', tdx, 'на', abs(dx),'.' ' По вертикали', tdy, 'на', abs(dy))
      elif dx!=0 and dy==0:
        print('По горизонтали', tdx, 'на', abs(dx),'.' ' По вертикали', tdy)
      elif dx==0 and dy!=0:
        print('По горизонтали', tdx,'.' ' По вертикали', tdy, 'на', abs(dy))
      else:
        print('По горизонтали', tdx,'.' ' По вертикали', tdy)

p1=trtl()
p1.count_moves(3,5)
p1.evolve()
p1.count_moves(8,2)
