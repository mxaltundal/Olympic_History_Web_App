# app.py
# Flask uygulaması - Python dosyası olarak çalıştırılmalıdır

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Veritabanı bağlantısı
DB_PATH = 'olympics.db'

def get_countries():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT country FROM Olympic_Country ORDER BY country")
        return [row[0] for row in cur.fetchall()]

def get_years():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT year FROM Olympic_Games ORDER BY year")
        return [row[0] for row in cur.fetchall()]

def get_sports():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT sport FROM Olympic_Results ORDER BY sport")
        return [row[0] for row in cur.fetchall() if row[0] is not None]

def get_filtered_results(country=None, year=None, sport=None):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        base_query = '''
        SELECT 
            CASE 
                WHEN ab.name IS NOT NULL THEN ab.name
                WHEN r.result_detail IS NOT NULL AND r.result_detail != 'na' THEN r.result_detail
                ELSE 'Unknown'
            END AS athlete_name,
            r.sport,
            g.year,
            r.result_description
        FROM Olympic_Results r
        JOIN Olympic_Games g ON r.edition_id = g.edition_id
        LEFT JOIN Olympic_Athlete_Event_Results aev ON r.result_id = aev.result_id
        LEFT JOIN Olympic_Athlete_Bio ab ON aev.athlete_id = ab.athlete_id
        WHERE 1=1
        '''

        filters = []
        params = []

        if year:
            filters.append("g.year = ?")
            params.append(year)
        if sport:
            filters.append("r.sport = ?")
            params.append(sport)
        if country:
            filters.append("r.result_description LIKE ?")
            params.append(f"%{country}%")

        if filters:
            base_query += " AND " + " AND ".join(filters)

        cur.execute(base_query, params)
        return cur.fetchall()

@app.route("/", methods=["GET", "POST"])
def homepage():
    countries = get_countries()
    years = get_years()
    sports = get_sports()
    results = []
    selected_country = selected_year = selected_sport = None
    no_results = False

    if request.method == "POST":
        selected_country = request.form.get("country") or None
        selected_year = request.form.get("year") or None
        selected_sport = request.form.get("sport") or None
        results = get_filtered_results(selected_country, selected_year, selected_sport)
        if not results:
            no_results = True
    else:
        # Sayfa ilk yüklendiğinde tüm kayıtları göster
        results = get_filtered_results()

    return render_template("homepage.html",
                           countries=countries,
                           years=years,
                           sports=sports,
                           results=results,
                           selected_country=selected_country,
                           selected_year=selected_year,
                           selected_sport=selected_sport,
                           no_results=no_results)

if __name__ == "__main__":
    app.run(debug=True)
