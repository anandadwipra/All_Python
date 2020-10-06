import sqlite3
conn = sqlite3.connect('user.db')
c = conn.cursor()
# Create table
def start(status,x):
	try:
		c.execute('''CREATE TABLE User
	    	         (userid INTEGER NOT NULL PRIMARY KEY , username text,email text,pass text)''')
		# i=1
	except:
		if status=="daftar":
			c.execute(f"SELECT username FROM User where username == '{x[0]}'")
			if len(c.fetchall())>=1:
				print("Masuk 1")
				return [f"{x[0]} already "," Please Use Another Username"]
			c.execute(f"SELECT username FROM User where email == '{x[1]}'")
			if len(c.fetchall())>=1:
				print("Masuk 2")
				return [f"{x[1]} already "," Please Use Another Email"]
			c.execute("SELECT userid FROM User ORDER BY userid")
			return (c.fetchall()[-1][0])+1
		else:
			c.execute(f"SELECT * FROM User WHERE username == '{x[0]}'")
			zz=c.fetchall()
			if len(zz)>=1 and zz[0][3]==x[1]:
				print("berhasil")
				return ["Main"]
			else:
				return ["Login"," Invalid Username or Password"]

# Insert a row of data
def add_user(x):
	i=start("daftar",x)
	if isinstance(i,list) :
		return i
	try:
		c.execute(f"INSERT INTO User VALUES ({i},'{x[0]}','{x[1]}','{x[2]}')")
		# c.execute(f"INSERT INTO User VALUES ({i},'Admin123','admin@yahoo.com','admin123')")
		conn.commit()
		return ["Succes :",f"{x[0]} berhasil didaftarkan"]
	except:
		print("fail")
def login(x):
	return (start("login",x))
# c.execute(f"INSERT INTO User VALUES ({i},'Admin123','admin@yahoo.com','admin123')")
def close():
	conn.close() 
# Save (commit) the changes

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
