from ks import ks # the klocksnack script
import time

searchWords = ['omega', 'cartier', 'constellation', '168.005', '167.005', 'santos']
klocksnack = ks(searchWords)
klocksnack.update()
trynbr = 0
while True:
  klocksnack.update()
  trynbr = trynbr + 1
  print(f'Update number: {trynbr}')
  time.sleep(10)
  
