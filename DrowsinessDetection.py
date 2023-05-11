import cv2
import numpy as np
import winsound

class DrowsinessDetector:
    def __init__(self, threshold = 0.25, consecutive_frames = 20):
        self.threshold = threshold
        self.consecutive_frames = consecutive_frames
        self.frame_counter_eyes = 0
        self.frame_counter_mouth = 0
        self.eye_aspect_ratio_threshold = 0.45
        self.yawn_threshold = 0.375
        self.yawn_count = 0
        self.eyes_closed_count = 0              
        
        # Load classifiers for face detection and eye detection
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('haarcascade_eyeglass.xml')
        self.mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

    def eye_aspect_ratio(self, eye):
        # Use this if you are using dlib library to detect 6 eye coordinates
        A = np.linalg.norm(eye[1]-eye[5])
        B = np.linalg.norm(eye[2]-eye[4])
        C = np.linalg.norm(eye[0]-eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
    
    def mouth_aspect_ratio(self,mouth):
        # Use this if you are using dlib library to detect 8 mouth coordinates
        A = np.linalg.norm(mouth[1]-mouth[7])
        B = np.linalg.norm(mouth[2]-mouth[6])
        C = np.linalg.norm(mouth[3]-mouth[5])
        D = np.linalg.norm(mouth[0]-mouth[4])
        mar = (A+B+C)/(2*D)
    
    def faces_detector(self, gray):        
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
    
    def eye_ROI_detector(self, roi_gray):
        eyes = self.eye_cascade.detectMultiScale(roi_gray)
        return eyes
       
    def check_blink_rate_threshold(self, avg_eye_aspect_ratio):
        if avg_eye_aspect_ratio < self.eye_aspect_ratio_threshold:
                self.frame_counter += 1
                if self.frame_counter >= self.consecutive_frames:
                    print("Eyes closed for too long")
                    return True
        else:
            self.frame_counter = 0

    def calculate_drowsiness_score(self):
        ear_score = self.eyes_closed_count / 5.0
        yawn_score = self.yawn_count / 5.0
        score = ear_score + yawn_score   
        if score > self.eye_aspect_ratio_threshold:
            return "Drowsy"
        else:
            return "Not drowsy"
    
    def detect(self, frame):           
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            # Extract ROI for eyes
            roi_gray = gray[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi_gray,1.3,5) 
            
            # Compute eye aspect ratio (EAR) for both eyes
            ear_left = 0
            ear_right = 0
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(frame, (ex+300, ey+100),(ex + ew + 300, ey + eh + 100), (128, 0, 255), 2)
                if ex < w//2:                
                    ear_left = eh/ex
                else:
                    ear_right = eh/ex
     
            ear_avg = (ear_left + ear_right) / 2
            
            # Check if EAR is below threshold
            if ear_avg < self.eye_aspect_ratio_threshold:
                self.frame_counter_eyes += 1
                if self.frame_counter_eyes >= self.consecutive_frames:
                    self.eyes_closed_count += 1
                    cv2.putText(frame,"Eyes Closed for too long !!!",(5,height-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),1,cv2.LINE_AA)
                    return True
            else:
                self.frame_counter_eyes = 0

            # Check if driver is yawning
            mouth_rects = self.mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))    
          
            for (mx, my, mw, mh) in mouth_rects:                                       
                if (mh/mx) > self.yawn_threshold:
                    self.frame_counter_mouth += 1
                    if self.frame_counter_mouth >= 8:
                        self.yawn_count += 1                        
                        cv2.putText(frame,"Yawn Detected !!!",(10,height-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,0),1,cv2.LINE_AA)
                        return True
                else:
                    self.frame_counter_mouth = 0                
        return False        

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = DrowsinessDetector(threshold=0.25,consecutive_frames=20)
    detector.eyes_closed_count = 0
    detector.yawn_count = 0
    while True:
        global frame
        ret, frame = cap.read()    
        height,width = frame.shape[:2]         
        res = detector.detect(frame)
        cv2.putText(frame,'Drowsiness count:'+str(detector.eyes_closed_count),(100,height-45), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),1,cv2.LINE_AA)
        cv2.putText(frame,'Yawn count:'+str(detector.yawn_count),(100,height-20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
        if(res == True):
            # Play a beep sound
            winsound.Beep(500, 2000)  # frequency, duration in milliseconds
        score = detector.calculate_drowsiness_score()      
        cv2.imshow("SafeDrive: Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()