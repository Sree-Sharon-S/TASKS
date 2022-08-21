from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="mypassword")
cursor = mydb.cursor()

cursor.execute("create database GROCERIES2")
cursor.execute("create table GROCERIES2.FRUITS(Name varchar(30), Quantity int, Rate int, TotalPrice int )")

app = Flask(__name__)


# to insert a new record into the table
@app.route('/xyz1', methods=['GET', 'POST'])
def inserting():
    name_var = request.json["name_var"]
    qty = request.json["qty"]
    rte = request.json["rte"]
    prc = request.json["prc"]

    import mysql
    import mysql.connector as conn
    mydb = conn.connect(host="localhost", user="root", passwd="mypassword")
    cursor = mydb.cursor()

    cursor.execute(
        f"insert into GROCERIES2.FRUITS(Name, Quantity, Rate, TotalPrice) values('{name_var}', {qty}, {rte}, {prc})")
    mydb.commit()
    return "The database has been updated"


# to delete a record if the column name is specified.
@app.route('/xyz2', methods=['GET', 'POST'])
def deleting():
    import mysql.connector as conn
    mydb = conn.connect(host='localhost', user='root', passwd="mypassword")
    cursor = mydb.cursor()

    if request.method == 'POST':
        name = request.json["FruitName"]
        cursor.execute(f"delete from GROCERIES2.FRUITS where Name = '{name}'")
        mydb.commit()
        return "The record is deleted"


# to update Rate of the item inside the table
@app.route('/xyz3', methods=["GET", 'POST'])
def updating():
    import mysql.connector as conn
    mydb = conn.connect(host='localhost', user='root', passwd="mypassword")
    cursor = mydb.cursor()

    if request.method == 'POST':
        new_value = request.json["new_value"]
        col_name = request.json["if_column"]
        col_value = request.json["column_value"]

        cursor.execute(f''' UPDATE GROCERIES2.FRUITS
                       SET Rate = {new_value} , TotalPrice = {new_value} * Quantity
                       WHERE {col_name} = '{col_value}' ''')

        mydb.commit()
        return "The record is updated"


# to fetch a record from table
@app.route('/xyz4', methods=["GET", "POST"])
def fetching():
    import mysql.connector as conn
    mydb = mydb = conn.connect(host='localhost', user='root', passwd="mypassword")
    cursor = mydb.cursor()

    if request.method == 'POST':
        cursor.execute("Select * from Groceries2.Fruits")

        myJson = {}
        for i in cursor.fetchall():
            myJson.update({"Name":i[0],"Quantity":i[1], "Rate": i[2], "TotalPrice":i[3]})
        return myJson

if __name__ == '__main__':
    app.run()
