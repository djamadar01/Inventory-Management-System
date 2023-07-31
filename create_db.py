import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid integer primary key autoincrement,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice integer primary key autoincrement,name text,contact text,desc text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid integer primary key autoincrement,name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid integer primary key autoincrement,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()
    
    
    
create_db()