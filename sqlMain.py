from sql import sqlClass

obj = sqlClass()
obj.createTable()
obj.insertVaribleIntoTable(2, 'Joe', 'joe@pynative.com', '2019-05-19', 9000)
obj.insertVaribleIntoTable(3, 'Ben', 'ben@pynative.com', '2019-02-23', 9500)
obj.fetchDatabase()
if obj.checkDatabase(2):
    print("Recieved True on id = 2")
if obj.checkDatabase(10):
    print("Recieved True on id = 10")


