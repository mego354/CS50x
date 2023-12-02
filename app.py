#please edit the location of the universty by adjusting the college_longitude, college_latitude
#
#                                   in line 193,194
import os
import sqlalchemy
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import csv
from helpers import apology, login_required
from lecturess import lecturess
from pytz import timezone
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///student.db")

filer2 = open("lectures.csv", "r")
lecturess(filer2)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
############################################

@app.route("/")
@login_required
def index():
    """Show portfolio """
    user_id = session["user_id"]
    student_db = db.execute(
        "SELECT id, name, attendance, CYBER, ENGLISH, PYTHON, MATHS, IT, PHYSICS FROM student WHERE id = ?",
        user_id,
    )
    if user_id != 6: #ADJUST FOR ADMIN ID
        n = student_db[0]["name"]
        flash(f"welcome {n} !")
        return render_template("index.html", database=student_db)
    else :
        look = db.execute(
            "select id, name, attendance, CYBER, ENGLISH, PYTHON, MATHS, IT, PHYSICS from student; ")
        n = student_db[0]["name"]
        flash(f"welcome {n} !")
        return render_template("index.html", database=student_db, look=look, look2=look[0])

#########################################

@app.route("/history")
@login_required
def history():
    """Show history """
    user_id = session["user_id"]
    history_db = db.execute(
        "SELECT *  FROM submit WHERE id = ? ORDER by time DESC",
        user_id,
    )
    time2 = datetime.datetime.now(timezone('Egypt'))
    time2 = time2.strftime("%y")
    flash("! Take a good look !")
    return render_template("history.html", database=history_db, time2=time2)

#########################################
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM student WHERE name = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

##########################

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Must write a username")
        elif not password:
            return apology("Must write a password")
        elif not confirmation:
            return apology("Must write a confirmation")
        elif password != confirmation:
            return apology("please confirm the password correctly")
        else:
            new = db.execute("SELECT * FROM student WHERE name = ?", username)
            if not new:
                hash = generate_password_hash(password)
                new_user = db.execute(
                    "INSERT INTO student (name, hash) VALUES (?, ?)", username, hash
                )
            else:
                return apology("Username already exists")

        session["user_id"] = new_user

        return redirect("/")

#########################################

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

############################################

@app.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "GET":
        return render_template("password.html")
    else:
        oldpassword = request.form.get("old_password")
        newpassword = request.form.get("new_password")
        confirmation = request.form.get("confirmation")
        user_id = session["user_id"]

        dat0= db.execute(
            "SELECT * FROM student WHERE id = ?", user_id
        )


        if not oldpassword or not check_password_hash(
            dat0[0]["hash"], oldpassword
        ):
            return apology("invalid old password", 403)

        elif not newpassword:
            return apology("Must write a new password")
        elif not confirmation:
            return apology("Must write a confirmation")
        elif newpassword != confirmation:
            return apology("please confirm the password correctly")
        else:
            hash = generate_password_hash(newpassword)
            db.execute("UPDATE student SET hash = ? WHERE id = ?", hash, user_id)

        return redirect("/")

#################################3


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        timee = datetime.datetime.now(timezone('Egypt'))
        now_d = timee.strftime("%d")
        now_d = int(now_d)
        now_m = timee.strftime("%m")
        now_m = int(now_m)
        table = db.execute("SELECT * FROM lectures WHERE month = ? and day = ?", now_m, now_d)
        return render_template("quote.html", table=table)
    else:
###################################
                        #######################!un comment location code! ###################333


        # latitude = request.form.get('latitude')
        # longitude = request.form.get('longitude')
        #         #31.203138161664704, 29.879468582284993 testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # # Assuming college coordinates, replace with the college's coordinates
        # college_latitude = 31.203138161664704
        # college_longitude = 29.879468582284993
        # try:
        #     # Calculate distance (you may want to use a more accurate algorithm)
        #     distance = ((float(latitude) - college_latitude)**2 + (float(longitude) - college_longitude)**2)**0.5

        #     # Assuming a threshold of 0.01 for simplicity (adjust as needed)
        #     if distance > 0.01:
        #         return apology("Attendance rejected. You are too far from the college.")
        # except ValueError:
        #     print(latitude)
        #     print(longitude)
        #     return apology("OPEN THE LOCATION PlEASE.")


####################################
        symbol = request.form.get("symbol")

        file = open("lectures.csv", "r")
        fi_le = csv.DictReader(file)
        timee = datetime.datetime.now(timezone('Egypt'))
        now_d = timee.strftime("%d")
        now_d = int(now_d)
        now_m = timee.strftime("%m")
        now_m = int(now_m)
        if not symbol:
            return apology("Write a symbol please")

        for row in fi_le:
            if row["name"] == symbol :
                if now_d == int(row["day"]) and now_m == int(row["date"]):
                    namee = row["name"]
                    date = int(row["date"])
                    day = int(row["day"])
                    time = int(row["hour"])
                    now_h = int(timee.strftime("%H"))

                    if now_h < time:
                        flash(timee)
                        return apology("this lecture's time is NOT now")
                    elif now_h > time + 17:
                        return apology("unfortunatelly you have missed this class!")
                    elif now_h == time or now_h <= time + 17 :


                        file.close()
                        session["symbol"] = symbol
                        session["month"] = date
                        session["day"] = day
                        session["hour"] = time
                        return render_template(
                        "quoted.html",
                        name=namee,
                        date=date,
                        day=day
                        )

        db.execute("DELETE FROM lectures WHERE name = ? and month = ? and day = ? ", symbol, now_m, now_d)
        file.close()
        return apology("This lecture is NOT today")

#########################

@app.route("/quoted", methods=["GET", "POST"])
@login_required
def quoted():
    """Get quoted"""
    if request.method == "GET":
        return render_template("quoted.html")
    else:
        user_id = session["user_id"]
        lecture = session.get("symbol")
        month = session.get("month")
        day = session.get("day")
        hour = session.get("hour")

        first = db.execute("SELECT attend FROM SUBMIT WHERE id = ? and lecture = ? and month = ? and day = ? and hour = ?",user_id, lecture, month, day, hour)

        if first:
            return apology("you,ve submitted before")
        else:
            time1 = datetime.datetime.now(timezone('Egypt'))
            db.execute(
                    "insert into submit (id,lecture,month,day,hour,time) VALUES (?,?,?,?,?,?)",
                    user_id,
                    lecture,
                    month,
                    day,
                    hour,
                    time1
                )

            db.execute("UPDATE submit SET attend = ? WHERE id = ? and lecture = ? and month = ? and day = ? and hour = ?", 1, user_id, lecture, month, day, hour)

            attendd = db.execute(
                "SELECT attendance FROM student WHERE id = ?", user_id)
            attend = attendd[0]["attendance"]
            db.execute("UPDATE student SET attendance = ? WHERE id = ?", attend + 1, user_id)


            if lecture == "ENGLISH":
                score = db.execute("SELECT ENGLISH FROM student WHERE ID = :d", d=user_id)
                score = score[0]["ENGLISH"]
                db.execute("UPDATE student SET ENGLISH = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")

            elif lecture == "PYTHON":
                score = db.execute("SELECT PYTHON FROM student WHERE ID = :d", d=user_id)
                score = score[0]["PYTHON"]
                db.execute("UPDATE student SET PYTHON = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")

            elif lecture == "IT":
                score = db.execute("SELECT IT FROM student WHERE ID = :d", d=user_id)
                score = score[0]["IT"]
                db.execute("UPDATE student SET IT = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")

            elif lecture == "MATHS":
                score = db.execute("SELECT MATHS FROM student WHERE ID = :d", d=user_id)
                score = score[0]["MATHS"]
                db.execute("UPDATE student SET MATHS = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")

            elif lecture == "PHYSICS":
                score = db.execute("SELECT PHYSICS FROM student WHERE ID = :d", d=user_id)
                score = score[0]["PHYSICS"]
                db.execute("UPDATE student SET PHYSICS = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")

            elif lecture == "CYBER":
                score = db.execute("SELECT CYBER FROM student WHERE ID = :d", d=user_id)
                score = score[0]["CYBER"]
                db.execute("UPDATE student SET CYBER = :a WHERE id = :d ", a = score + 1, d=user_id)
                return redirect("/")
            else :
                return apology("ERROOOOOOR")

if __name__ == '__main__':
 app.debug = True
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)


####################################################
