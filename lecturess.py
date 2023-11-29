import csv
from cs50 import SQL

db2 = SQL("sqlite:///student.db")


def lecturess(filer2):
    # filer2 = open("lectures.csv", "r")
    file2 = csv.DictReader(filer2)
    lecs2 = db2.execute("SELECT id FROM lectures")
    lectures_id_db2 = []
    for lec in lecs2:
        lec = lec["id"]
        lectures_id_db2.append(lec)

    for row in file2:
        row["id"] = int(row["id"])
        row["date"] = int(row["date"])
        row["day"] = int(row["day"])
        row["hour"] = int(row["hour"])

        if not row["id"] in lectures_id_db2:
            db2.execute(
                "insert into lectures (id,name,month,day,hour) VALUES (?,?,?,?,?)",
                row["id"],
                row["name"],
                row["date"],
                row["day"],
                row["hour"],
            )

        else:
            chk = db2.execute("select * FROM lectures WHERE id = ?", row["id"])
            idd = int(chk[0]["id"])
            nm = chk[0]["name"]
            mo = int(chk[0]["month"])
            da = int(chk[0]["day"])
            ho = int(chk[0]["hour"])
            if (
                nm == row["name"]
                and mo == row["date"]
                and da == row["day"]
                and ho == row["hour"]
            ):
                # print(idd, row["id"])
                continue
            elif (
                nm != row["name"]
                or mo != row["date"]
                or da != row["day"]
                or ho != row["hour"]
            ):
                db2.execute(
                    "UPDATE lectures SET name = :n, month = :m, day = :d, hour = :h WHERE id = :dd ;",
                    n=row["name"],
                    m=row["date"],
                    d=row["day"],
                    h=row["hour"],
                    dd=row["id"],
                )
    filer2.close()
