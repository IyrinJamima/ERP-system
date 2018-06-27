from flask import Flask
app = Flask(__name__)
import MySQLdb
connection = MySQLdb.connect(host="localhost", # The Host
                      user="root", # username
                      passwd="root", # password
                      db="customerprod") # name of the data base
cursor = connection.cursor()
	
@app.route('/product',methods = ["DELETE"])
def prod():
    description = 'perfume';
    del_prod = ("delete from products where description = 'perfume' " )
    cursor.execute(del_prod)
    connection.commit()
    return description

if __name__ == '__main__':	
       app.run()
	
