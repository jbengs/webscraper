from ks import ks
from gmail import Gmail

gmail = Gmail()
print("Before list labels: ")
gmail.listLabels()
print("Before send email: ")
gmail.sendEmail()

#searchWords = ['oris']
#klocksnack = ks(searchWords)
#klocksnack.update()

