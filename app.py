from flask import Flask, request
from flask_mysqldb import MySQL
import view

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

@app.route('/')
def homepage():
    return view.homePage()

@app.route('/search', methods=['GET'])
def search():
    filter_value = request.args.get('filter', '')

    if not filter_value:
        return 'Filter parameter is empty.'

    # Initialize cursor outside the try block
    cursor = mysql.connection.cursor()

    try:
        # Using parameterized query to prevent SQL injection
        sorgu = "SELECT * FROM olympic_athlete_bio WHERE name=%s"
        query_params = (filter_value,)

        cursor.execute(sorgu, query_params)
        data = cursor.fetchall()
        return str(data)

    except MySQLdb.Error as err:
        return f"Error: {err}"

    finally:
        # Close the cursor in the finally block
        cursor.close()

    return 'Burcak sal bizi'

if __name__ == '__main__':
    app.run(debug=True)
