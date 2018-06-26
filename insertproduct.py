from flask import Flask
app = Flask(__name__)
import MySQLdb
connection = MySQLdb.connect(host="localhost", # The Host
                      user="root", # username
                      passwd="root", # password
                      db="customerprod") # name of the data basepro.py

cursor = connection.cursor()
	
@app.route('/prod',methods = ["GET"])
def prod():
    name = 'dress';
    productcode = 555;
    description = 'dress';
    price = 500;
    cursor.execute("insert into products (name, productcode, description, price) values ('"+ name +"'," + str(productcode) + ",'" + description +"'," + str(price) +")")
    connection.commit()
    return name

if __name__ == '__main__':
       app.run()
	
