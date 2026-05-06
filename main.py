#call needed dependencies
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#give the vc a nickname
capture = cv2.VideoCapture(0)

#resize the video capture to the highest supported quality (720p)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

objd = mp.solutions.object_detection
detector = objd.ObjectDetection(min_detection_confidence=0.5)

while True:

	success, frame = capture.read()

	#if q key pressed, close the program
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	if success:
		
		rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		results = detector.process(rgb_frame)
	
		if results.detections:
		  for detection in results.detections:
		    for category in detection.label:
		      print(f"I see a: {category}")
          cv2.putText(frame, f"{category}", (50,50),
          cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

		#create a new window labeled "camera" and displays the camera inside it
		cv2.imshow("camera", frame)

