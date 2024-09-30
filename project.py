import cv2 
import face_recognition


#load known face recognition and names

known_face_encodings =  []
known_face_names = []

# load known faces and their names here 
known_person1_image = face_recognition.load_image_file('Elon_musk.jpg')
known_person1_image = face_recognition.load_image_file('Mark-Zuckerberg.jpg')
known_person1_image = face_recognition.load_image_file('bill_gates.jpg')

known_person1_enconding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_enconding = face_recognition.face_encodings(known_person1_image)[0]
known_person3_enconding = face_recognition.face_encodings(known_person1_image)[0]

known_face_encodings.append(known_person1_enconding)
known_face_encodings.append(known_person2_enconding)
known_face_encodings.append(known_person3_enconding)

known_face_names.append("Elon_musk.jpeg")
known_face_names.append('Mark-Zuckerberg.jpg')
known_face_names.append('bill_gates.jpg')

# inintialize webcam

video_cap = cv2.VideoCapture(0)

while True : 
    # Capture frame-by-frame
    ret, frame = video_cap.read()
    
    # find all faces locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_recognition)
    
    #Loop through each face found in the frame
    for (top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):
        #Check if the face matches any known faces
        matches = face_encodings.compare_faces(known_face_encodings , face_encodings)
        name = "Unknown"
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        # Draw a box around the face and label with name
        
        cv2.rectangle(frame, (left, top), ( right , bottom) , (0,0,255) , 2 )
        cv2.putText(frame, name , (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9 , (0,0,255) , 2)
        
# display the resulting frame 
    cv2.imshow('video' , frame)
    
# break the loop when the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    

# Relsease the webcam and close opencv windows
video_cap.release()
cv2.destroyAllWindows()