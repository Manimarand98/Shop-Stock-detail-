from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'db[mysql_localhost]'
app.config['MYSQL_USER'] = 'db[mysql_root]'
app.config['MYSQL_PASSWORD'] = 'db[mysql_maruthu]'
app.config['MYSQL_DB'] = 'db[mysql_insidewindow]'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        #Fetch from data
        stockdetails = request.form
        productid =stockdetails['name']
        productname = stockdetails['name']
        warehouse = stockdetails['name']
        Qty = stockdetails['name']
        cur = mysql.connection.cursor()
        cur.execute("insert into stock(productid,'productname', 'warehouse', 'Qty') values(%S, %S, %S, %s)",('productid', 'productname', 'warehouse', 'Qty'))
        mysql.connection.commit()
        cur.close()
        return redirect('/stock')
        return render_template('product.html')
    @app.route('/stock')
    def stock():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("Select * from stock")
        if resultValue >0:
            stockdetails = cur.fetchall()
        return render_template('stock.html', stockdetails=stockdetails)
if __name__ == '__main__':
    app.run(debug=True)