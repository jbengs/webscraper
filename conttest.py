
from ksController import ksController

obj = ksController()
obj.createTable()
obj.insertVaribleIntoTable('Universal Geneve White Shadow (4,5k)', 'Epicure.watches', 13406, '/members/epicure-watches.13406/')
obj.fetchDatabase()
if obj.checkDatabase('Universal Geneve White Shadow (4,5k)'):
    print("Recieved True on existing")
if not obj.checkDatabase('Universal Geneve'):
    print("Recieved False on non existent")


