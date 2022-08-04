from ks import ks #Klocksnack.se
from uhrforum import uhrforum #Uhrforum.de
from omegaforums import omegaforums #omegaforums
import time

#Must be lowercase!
searchWords = ['omega', 'cartier', 'constellation', '168.005', '167.005', 'santos']
updateNbr = 1
timeout = 300 #seconds

print(f'----------------------------\nWelcome to the server!\nSETTINGS\n - Frequency: {timeout} seconds\n - Sites: Klocksnack, Uhrforum, Omegaforums\n - Searchwords: {searchWords}\n - Email to: bengs.joel@gmail.com\n')
print('Datatables: ')
klocksnack = ks(searchWords)
uhrforum = uhrforum(searchWords)
omegaforums = omegaforums(searchWords)
print('----------------------------\n')

while True:
  print(f'\n---Update number: {updateNbr}, timeout {timeout} seconds---')

  print('\n---Klocksnack.se---')
  klocksnack.update()

  print('\n---UhrForum.de---')
  uhrforum.update()

  print('\n---OmegaForums.net---')
  omegaforums.update()

  updateNbr = updateNbr + 1
  time.sleep(timeout)
