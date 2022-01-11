#
# Pylint Example
#

class car:
  def __init__(self, color):
    self.color = color
    
    
my_car = car('Blue')

def    crash(car1, car2) :
        car1.color= 'Burnt'

crash(car('red'), my_car)