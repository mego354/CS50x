# BATU Attendance

## Video Demo
[Watch the video demonstration](https://youtu.be/oVbF4yntRyc)

## Description
BATU Attendance is a web application developed as the final project for CS50x. It aims to efficiently manage student attendance by implementing controls over:

1. Who can submit their attendance.
2. When attendance submissions can occur.
3. The specific location where attendance is submitted.
4. Storage of attendance data.
5. Management and utilization of stored data.

## Implementation Steps
### 1. Build a Simple Web Application
The initial step involves creating a web application with the necessary functionalities.

### 2. Set Permissions
Assign appropriate permissions to ensure the smooth operation of subsequent steps.

### 3. Database Setup
Establish a robust database to store and manage attendance data.

### 4. Data Collection
Collect data from the web application and store it in the database.

### 5. Daily Data Management
Assign a specialist to manage the daily data handling tasks for both the web page and the database.

## Web Application Features
The web application includes the following pages:

- **Register Page**
- **Login Page**
- **Attendance Page**
- **History Page**
- **Reset Password Page**

### Attendance Page Details
The Attendance Page is specifically designed for data submission by students, overseen by a specialist. Key functionalities include:

- A submit button that students can click when it appears for them.
- The submit button records the date and location of the submission.
- The backend database stores all submitted data.

## Detailed Workflow
- **User Interaction**: Students log in and interact with the Attendance Page.
- **Backend Operations**: 
  - Modify the lectures displayed to the students.
  - Design a method for easy data collection and modification.
  - Ensure location data is stored to prevent manipulation.
  - Link each account to a student ID using session data ("cookies").
  - Enforce location-based attendance within the university area.

### Final Output
- Each student has a profile with their data and attendance history.
- A daily lecture schedule is available on the web page.
- The database holds a comprehensive attendance history for each student.
- A streamlined and effective solution for attendance data collection and problem-solving.

## Database Structure
The database consists of three tables: `student`, `lectures`, and `submit`.

### Student Table
- Rows: Each student by ID and name.
- Courses: Physics, Python, English, IT, Mathematics, Cyber Security.
- Updates: When a student submits attendance, both the course-specific score and overall attendance count increase.

### Lectures Table
- Updates with each page refresh, fetching data from `lectures.csv`.
- Admins can add lectures by specifying the name, date, and time.
- Students can submit attendance if the current date and time match the lecture schedule and they are within the university area.

### Submit Table
- Records each attendance submission.
- Facilitates easy retrieval of attendance records for professors by student ID and lecture name.

## Testing Note
- **Location Determination**: Disabled to allow access for everyone.
- **Attendance Time Limit**: Extended to 18 hours instead of 2 for testing purposes.
