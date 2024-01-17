# python -m pip install opencv-python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) # 높이

# 얼굴인식 모델 가져오기 
face_cascade = cv2.CascadeClassifier("data\haarcascades\haarcascade_lefteye_2splits.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    faces = face_cascade.detectMultiScale(frame, 1.03 , 5)
    
    for x,y,w,h in faces:
        print(x,y,w,h)
        # 사각형을 그려보시오 
    cv2.imshow("VideoFrame", frame) # imshow : 보여주기 


capture.release()
cv2.destroyAllWindows()