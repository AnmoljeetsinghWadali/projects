import sqlite3 as sql
def connect():
    conn=sql.connect('hotel.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hotel(id INTEGER PRIMARY KEY,name TEXT,address TEXT,phoneno INTEGER,days INTEGER,roomtype TEXT,amount INTEGER)")
    conn.commit()
    conn.close()
    
def insert(name,address,phoneno,days,roomtype,total):
    
    conn=sql.connect('hotel.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('INSERT INTO hotel VALUES(NULL,?,?,?,?,?,?)',(name,address,phoneno,days,roomtype,total))
    conn.commit()
    conn.close()
    print('data added')
total=0  


def view():

    conn=sql.connect('hotel.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM hotel')
    ans=cur.fetchall()
    conn.close()
    print(ans)

def search(name='',address='',phoneno='',days='',roomtype='',total='' ):
    conn=sql.connect('hotel.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM hotel WHERE name=? or address=? or phoneno=? or days=? or roomtype=? or amount=?',(name,address,phoneno,days,roomtype,total))
    ans=cur.fetchall()
    conn.close()
    return ans

def delete(i):
    
    conn=sql.connect('hotel.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM hotel WHERE id=?',(i))
    conn.commit()
    conn.close()
    
def update(name='',address='',phoneno='',days='',roomtype='',total='',i=''):
    
    conn=sql.connect('hotel.db')
    cur=conn.cursor()
    cur.execute('UPDATE hotel SET name=? or address=? or phoneno=? or days=? or roomtype=? or amount=? WHERE id=?',(name,address,phoneno,days,roomtype,total,i))
    conn.commit()
    conn.close()


    
#connect()
#insert('anmol123 ','asr',9888997293,10,'king',cal(10,'king'))
#print(view())
#update('anmol123 ','patiala',9888997293,100,'king',cal(100,'king'),1)
#print(view())
