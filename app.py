from ks import ks #Klocksnack.se
from uhrforum import uhrforum #Uhrforum.de
import time

#Must be lowercase!
searchWords = ['omega', 'cartier', 'constellation', '168.005', '167.005', 'santos']
trynbr = 1
timeout = 10

print(f'----------------------------\nWelcome to the server!\nSETTINGS\n - Frequency: {timeout} seconds\n - Sites: Klocksnack, Uhrforum\n - Searchwords: {searchWords}\n - Email to: bengs.joel@gmail.com\n')
print('Datatables: ')
klocksnack = ks(searchWords)
uhrforum = uhrforum(searchWords)
print('----------------------------\n')

while trynbr < 2:
  print(f'\n---Update number: {trynbr}---')

  print('\n---Klocksnack.se---')
  klocksnack.update()

  print('\n---UhrForum.de---')
  uhrforum.update()

  trynbr = trynbr + 1
  time.sleep(timeout)
