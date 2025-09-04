from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB for subscribers
def init_db():
    conn = sqlite3.connect("subscribers.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS subscribers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL)''')
    conn.commit()
    conn.close()

# Initialize DB for contacts
def init_contact_db():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT,
                  contact TEXT,
                  inquiry TEXT,
                  details TEXT)''')
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

# ✅ New route for contact form
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    contact = request.form["contact"]
    inquiry = request.form["inquiry"]
    details = request.form["details"]

    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, contact, inquiry, details) VALUES (?, ?, ?, ?, ?)",
              (name, email, contact, inquiry, details))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/wework')
def wework():
    return render_template("wework.html")

@app.route('/project_1')
def project_1():
    return render_template("project_1.html")

@app.route('/project_2')
def project_2():
    return render_template("project_2.html")

@app.route('/project_3')
def project_3():
    return render_template("project_3.html")

@app.route('/project_4')
def project_4():
    return render_template("project_4.html")

@app.route('/project_5')
def project_5():
    return render_template("project_5.html")

@app.route('/project_6')
def project_6():
    return render_template("project_6.html")

@app.route('/project_7')
def project_7():
    return render_template("project_7.html")

@app.route('/project_8')
def project_8():
    return render_template("project_8.html")

@app.route('/project_9')
def project_9():
    return render_template("project_9.html")

@app.route('/project_10')
def project_10():
    return render_template("project_10.html")

@app.route('/project_11')
def project_11():
    return render_template("project_11.html")

@app.route('/project_12')
def project_12():
    return render_template("project_12.html")

@app.route('/project_13')
def project_13():
    return render_template("project_13.html")

@app.route('/project_14')
def project_14():
    return render_template("project_14.html")

@app.route('/project_15')
def project_15():
    return render_template("project_15.html")

@app.route('/project_16')
def project_16():
    return render_template("project_16.html")

@app.route('/project_17')
def project_17():
    return render_template("project_17.html")

@app.route('/project_18')
def project_18():
    return render_template("project_18.html")

@app.route('/project_19')
def project_19():
    return render_template("project_19.html")

@app.route('/project_20')
def project_20():
    return render_template("project_20.html")

@app.route('/project_21')
def project_21():
    return render_template("project_21.html")

@app.route('/project_22')
def project_22():
    return render_template("project_22.html")

@app.route('/project_23')
def project_23():
    return render_template("project_23.html")

@app.route('/project_24')
def project_24():
    return render_template("project_24.html")

@app.route('/project_25')
def project_25():
    return render_template("project_25.html")

@app.route('/project_26')
def project_26():
    return render_template("project_26.html")


@app.route('/project_27')
def project_27():
    return render_template("project_27.html")

@app.route('/project_28')
def project_28():
    return render_template("project_28.html")

@app.route('/project_29')
def project_29():
    return render_template("project_29.html")

@app.route('/project_30')
def project_30():
    return render_template("project_30.html")

@app.route('/project_31')
def project_31():
    return render_template("project_31.html")

@app.route('/project_32')
def project_32():
    return render_template("project_32.html")

@app.route('/project_33')
def project_33():
    return render_template("project_33.html")

@app.route('/project_34')
def project_34():
    return render_template("project_34.html")
if __name__ == "__main__":
    init_db()
    init_contact_db()
    app.run(debug=True)
