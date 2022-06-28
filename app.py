from ks import ks # the klocksnack script
import time

searchWords = ['omega', 'cartier', 'constellation', '168.005', '167.005', 'santos']
klocksnack = ks(searchWords)
klocksnack.update()

while True:
  klocksnack.update()
  time.sleep(600)
  
