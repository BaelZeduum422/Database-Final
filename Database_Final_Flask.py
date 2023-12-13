from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask import redirect, url_for

app = Flask(__name__)

# MySQL configurations - Database credentials
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anime123!'
app.config['MYSQL_DB'] = 'Final_Database_Climate'

mysql = MySQL(app)

# Index route - Display main menu
@app.route('/')
def index():
    return render_template('index.html')

# Route to render the form for adding data
@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        year = request.form['year']
        season = request.form['season']
        temperature = request.form['temperature']
        predicted_temp = request.form['predicted_temp']
        area_id = request.form['area_id']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO YearlySeasonTemp (Area_ID, Year, Season, Temperature, Predicted_Temp) VALUES (%s, %s, %s, %s, %s)",
                    (area_id, year, season, temperature, predicted_temp))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_data'))
    return render_template('add.html')

# Route to render the form for selecting data to edit
@app.route('/select_to_edit', methods=['GET', 'POST'])
def select_to_edit():
    if request.method == 'POST':
        yearlyTempID = request.form['yearlyTempID']
        return redirect(url_for('edit_data', temp_id=yearlyTempID))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM YearlySeasonTemp")
    yearly_season_temps = cur.fetchall()
    cur.close()

    return render_template('select_to_edit.html', yearly_season_temps=yearly_season_temps)

# Route to edit specific data
@app.route('/edit/<int:temp_id>', methods=['GET', 'POST'])
def edit_data(temp_id):
    if request.method == 'POST':
        new_area_id = request.form['new_area_id']
        new_year = request.form['new_year']
        new_season = request.form['new_season']
        new_temperature = request.form['new_temperature']
        new_predicted_temp = request.form['new_predicted_temp']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE YearlySeasonTemp 
            SET Area_ID = %s, Year = %s, Season = %s, Temperature = %s, Predicted_Temp = %s 
            WHERE YearlyTemp_ID = %s
        """, (new_area_id, new_year, new_season, new_temperature, new_predicted_temp, temp_id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('view_data'))

    # Fetch data for the selected ID
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM YearlySeasonTemp WHERE YearlyTemp_ID = %s", (temp_id,))
    data = cur.fetchone()
    cur.close()

    if data is None:
        return "No data found for this ID"

    return render_template('edit.html', data=data)

# Route to render the form for selecting data to delete
@app.route('/select_to_delete', methods=['GET', 'POST'])
def select_to_delete():
    data = None
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM YearlySeasonTemp")
    yearly_season_temps = cur.fetchall()
    cur.close()

    if request.method == 'POST':
        yearlyTempID = request.form['yearlyTempID']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM YearlySeasonTemp WHERE YearlyTemp_ID = %s", (yearlyTempID,))
        data = cur.fetchone()
        cur.close()

    return render_template('select_to_delete.html', yearly_season_temps=yearly_season_temps, data=data)

# Route to delete specific data
@app.route('/delete_data/<int:temp_id>', methods=['POST'])
def delete_specific_data(temp_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM YearlySeasonTemp WHERE YearlyTemp_ID = %s", (temp_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('view_data'))

# Route to render the view data page
@app.route('/view')
def view_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM YearlySeasonTemp")
    yearly_season_temps = cur.fetchall()
    cur.execute("SELECT * FROM Area")
    areas = cur.fetchall()
    cur.close()
    return render_template('view.html', yearly_season_temps=yearly_season_temps, areas=areas)

if __name__ == '__main__':
    app.run(debug=True)
