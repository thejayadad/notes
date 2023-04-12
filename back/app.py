from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras



app = Flask(__name__)
app.secret_key = 'thejayadad'

conn = psycopg2.connect(host="localhost", dbname="notes", user="postgres", password='football', port=5432)
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS note (
    id INT PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(500)
)

                          """)


# insert_script = 'INSERT INTO note (id, title, description) VALUES (%s,%s,%s)'
# insert_value = (3, "Exercise", "Go to the gym after work")
# cur.execute(insert_script, insert_value)


conn.commit()


@app.route("/", methods=['GET'])
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    n = "SELECT * FROM note"
    cur.execute(n)
    list_notes = cur.fetchall()
    return render_template("index.html", list_notes = list_notes)



if __name__ == "__main__":
    app.run(debug=True)


# conn.close()
