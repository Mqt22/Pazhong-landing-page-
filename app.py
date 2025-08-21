from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("subscribers.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS subscribers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL)''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if email:
        conn = sqlite3.connect("subscribers.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
            conn.commit()
        except sqlite3.IntegrityError:
            pass  # ignore if email already exists
        conn.close()
    return redirect("/")  # back to homepage

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
