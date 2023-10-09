import sqlite3

def get_all_data():

    try:
        db = sqlite3.connect('app.db')
        print('connect To Database Successfully')

        cr = db.cursor()
        cr.execute('select * from users')
        results = cr.fetchall()
        print(f'Database Has {len(results)} Rows.')
        
        print('Showing Data:')
        for row in results:
            print(f'UserId => {row[0]}',end=' ')
            print(f'Username => {row[1]}')

    except sqlite3.Error as er :
        print(f'Error Reading Data {er}')

    finally:
        if (db):
            db.close()
            print('Connection To Database Is Closed')


get_all_data()
