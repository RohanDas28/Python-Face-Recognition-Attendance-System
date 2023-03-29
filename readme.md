# Python Face Recognition Attendance System
This is a face recognition based attendance system developed in Python. It uses the face_recognition library along with other modules to recognize faces and mark attendance in a CSV file.

## Requirements
```
tkinter
subprocess
csv
face_recognition
cv2
numpy
os
datetime
json
```

## Files
1. gui.py is the main file which contains the welcome screen with 3 buttons.
2. attendence_system.py registers attendance using face recognition.
3. AddStudent.py adds a student's name and photo to the database.
4. OpenCSV.py checks the attendance records.
5. face_images.json: These are the student names and their images saved in a JSON file which is read by AddStudent.py.

## How to Use

- Clone the repository or download the files.
- Install the required modules.
- Install Vistual Studio Build Tools and Install C++ Libraries there 
- Run gui.py file.
- From the welcome screen, select one of the three options:
  - Open Attendance to mark attendance.
  - Add Students to add a new student.
  - Check Attendance to view attendance records.
  - Follow the instructions on the screen to complete the desired action.
## Notes
Please ensure that the camera is working properly and there is sufficient lighting in the room for face recognition to work effectively.
Make sure that the student images are clear and there is no obstruction on the face.

## Todo
- [x] Finish initial app for synopsis
- [ ] Add Students Exit Attendance
- [ ] Add Students Database on entry 
- [ ] Fetch Students Details from Database
- [ ] Send Email to Parents when Attendance is Done  
- [ ] Show Press Q to exit on Attendance Windows Text


<br>
## Author
## [Rohan Das](rohandas28.github.io)
