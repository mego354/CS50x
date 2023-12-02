 BATU Attendance
 Video Demo:  <https://youtu.be/oVbF4yntRyc>
 Description:
     An idea for organizing student attendance management​:

WHAT WE NEED TO CONTROL​:
1.WHO CAN SUBMIT THEIR ATTENDANCE​
2.WHEN DOES THAT ACUALLY HAPPEN ​
3.DETRMINE A SPECIFIC LOCATION​
4.DETRMINE A WAY TO STORED DATA​
5.HOW TO DEAL WITH THE STORED DATA​

HOW TO DO THAT ?​
FIRST OF ALL : is to build a simple Web application​
THEN : give all the needed permissions to become handy for the next steps​
NO DOUBT : we need a perfect database​
AFTER THAT : we need to collect the data from that web in the --> DATABASE​
AS A FINAL STEP : must assign the daily tasks to a  specialist who would handle the page's data and the database as well ​

THE WEB APPLICATION​
WEB APPLICATION  MUST HAVE FIVE THING​
REGISTER PAGE ​
LOGIN PAGE​
ATTENDANCE PAGE​
HISTORY PAGE​
RESET PASSWORD PAGE​

​ATTENDACE PAGE​
THE ATTENDACE PAGE INFO:​
The only page that will get manipulated by the specialist ​
The student can click on submit button when it appears for them​
That submit button MUST provide the date and location by which it has been clicked​
In the backend of that page there is a database that would gain all of this data.​

DETAILS for how it works​:
We've handled the login part and how the user could activate with the page​
For the backend and the most important part :​
important to modify the lectures that appear for the student ​
Collecting the data would need a good method and design to be easily modified​
The most important thing is to find a way to store the location as well in the database​
To prevent any manipulating  from the students every account would be connected to the id while registering the account and that’s would be easy by the session's data "cookies"​ and while execute the attendance for any lecture the student MUST be in the universty's area

AS A FINAL LOOK WE CAN SEE:​
Every student has their own profile that contains their data and attendance history ​
A web page contains the lectures for the day​
Data base contains all history of attendance for each student id​
A perfect way to collect data and solve a problem in such a smooth way ​

databases contains 3 tables
student,lectures,submit
student contains row for every and each student by their id and name and 6 courses as physics, python, english, it, mathematics, cyber security they all get updated once the student vlick submit for any class to be added a 1 score for the class column and one for the attendance column because attendance column contains the amount of attendance in all classes togather
lectures table get updated every time the page refresh itself and it gets all the the data of lecturs from the lectures.csv file so the admin could add any lecture anytime just by typing the lecture's name, month,day,time and it be added to the database and any student could submit their attendace once the acual date,time is the same for the lecture and their location is in the universty area
submit table contains all the data for submiting classes for each student so that whenever any professor needs to get the amount of attendance of any student that would be easy by selecting the student id grouped by the lecture's name

USAGE: 
the admin has to modify the lectures every 3 months by opening lectures.csv 
then delete all lectures and write each subject with which it's id,month,day,hour only once for each subject
after that run python add.py which would add every lecture for the next 3 months 
restart running flask app 
done!
do not forget to adjust the location for the universty also the limit of hours during which the student would submit their attendance.

the app's been hosted for testing purpose at : http://megahd.pythonanywhere.com/
