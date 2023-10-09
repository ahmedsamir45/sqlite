import sqlite3 

db = sqlite3.connect('app.db')

cr = db.cursor()

cr.execute('CREATE TABLE if not exists skils (name text , progress integer , user_id integer)')
cr.execute('CREATE TABLE if not exists users (user_id integer,name text )')

cr.execute("insert into users(user_id,name) values(1,'Ahmed')")
cr.execute("insert into users(user_id,name) values(2,'Sayed')")
cr.execute("insert into users(user_id,name) values(3,'Osama')")

cr.execute('select name from users')


# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

print(cr.fetchall())
cr.execute("select * from skils")
print(cr.fetchall())
    
db.commit()


db.close()

