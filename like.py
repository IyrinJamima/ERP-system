from flask import Flask
app = Flask(__name__)
import MySQLdb
connection = MySQLdb.connect(host="localhost", # The Host
                      user="root", # username
                      passwd="root", # password
                      db="customerprod") # name of the data base
cursor = connection.cursor()

@app.route('/produ',methods = ["GET"])
def selectprod():
    name = 'dress';
    cursor.execute("select * from products where name like '%s%',likeString " )
    connection.commit()
    return name
	
if __name__ == '__main__':
       app.run()
		
