import csv
filer1 = open("lectures.csv", "r")
file1 = csv.DictReader(filer1)
keys = ["id","name","date","day","hour"]
defult = []
for file in file1:
    lecture = []
    lecture.append(file["id"])
    lecture.append(file["name"])
    lecture.append(file["date"])
    lecture.append(file["day"])
    lecture.append(file["hour"])
    defult.append(lecture)
filer1.close()
################################
lectures = []
for i in range(30):
    for lec in defult:
        lecture = []
        lecture.append(int(lec[0]) + (i * 6))
        lecture.append(lec[1])
        lecture.append(int(lec[2]))
        lecture.append(int(lec[3]) + i)
        lecture.append(lec[4])
        lectures.append(lecture)
################################
filer2 = open("lectures.csv", "w")
file2 = csv.writer(filer2)
file2.writerow(keys)
file2.writerows(lectures)
