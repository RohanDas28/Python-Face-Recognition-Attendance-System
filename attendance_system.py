import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
import json

# Open video capture
video_capture = cv2.VideoCapture(1)

# Load known face images and encodings
with open('face_images.json') as f:
    face_images = json.load(f)['faces']

known_face_encodings = []
known_face_names = []

for face_image in face_images:
    name = face_image['name']
    file_path = face_image['file_path']
    image = face_recognition.load_image_file(file_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Store known face encodings and names
known_faces_names = known_face_names

# Create a list of students who are expected to attend
students = known_faces_names.copy()

# Initialize variables for face detection and recognition
face_locations = []
face_encodings = []
face_names = []
s = True

# Get the current date for the attendance record
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Get the current directory path
current_directory = os.getcwd()

# Create a 'Records' folder if it doesn't exist
records_folder_path = os.path.join(current_directory, 'Records')
if not os.path.exists(records_folder_path):
    os.makedirs(records_folder_path)

# Create a CSV file to store attendance records for the day in the 'Records' folder
file_name = current_date + '.csv'
file_path = os.path.join(records_folder_path, file_name)
f = open(file_path, 'w+', newline='')
lnwriter = csv.writer(f)


# Start the video capture loop
while True:
    # Read a frame from the video capture
    _, frame = video_capture.read()

    # Resize the frame to speed up face detection and recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Detect and recognize faces
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # Compare face encodings to known face encodings to recognize faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)

            # Update attendance record and remove student from expected list
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name+' Present',bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

                if name in students:
                    print('Present')
                    students.remove(name)
                    print('Remaining Students:')
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

    # Display the attendance system window
    cv2.imshow("attendance system", frame)

    # Check for exit command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the attendance record file
video_capture.release()
cv2.destroyAllWindows()
f.close()
