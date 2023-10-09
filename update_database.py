import sqlite3 

db = sqlite3.connect('app.db')

cr = db.cursor()



cr.execute("update users set name = 'Mahmoud' where user_id = 1 ")
cr.execute("update users set name = 'Sayed' where user_id = 2 ")
cr.execute("update users set name = 'Ameer' where user_id = 3 ")

cr.execute("insert into users(user_id,name) values(4,'Gamal')")


cr.execute('delete from users where user_id = 4')



cr.execute('select * from users')


print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())



    
db.commit()


db.close()

