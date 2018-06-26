from flask import Flask
app = Flask(__name__)
import MySQLdb
connection = MySQLdb.connect(host="localhost", # The Host
                      user="root", # username
                      passwd="root", # password
                      db="customerprod") # name of the data base
cursor = connection.cursor()
	
@app.route('/pro',methods = ["PUT"])
def update_prod():	
    prod_name = 'brush';
    prod_id = 10;	  
    update_brush = "update products set name = 'brush' where productcode = 555"
    cursor.execute(update_brush)
    return prod_name	

if __name__ == '__main__':
       app.run()
	
