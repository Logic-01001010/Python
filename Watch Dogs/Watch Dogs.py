import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 720) # 윈도우 크기
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

#얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

count = 99

while(cap.isOpened()):
    
    if count != time.strftime('%H',time.localtime(time.time())): # 시간이 바뀌면 영상파일을 새로 만든다. (시간으로 감지)
        
        count = time.strftime('%H',time.localtime(time.time()))
        print('시간 변경 감지')
        
        out = cv2.VideoWriter(time.strftime('%Y-%m-%d %H시 %M분',time.localtime(time.time()))+'.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))

        print('파일 생성:',time.strftime('%Y-%m-%d %H시 %M분',time.localtime(time.time()))+'.avi')

    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 화면 반전 0: 상하, 1: 좌우

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         cv2.putText(frame, text='Detected', org=(x, y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)

   

    # 시간 텍스트 출력
    cv2.putText(frame, text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), org=(30, 450), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)


    cv2.imwrite(time.strftime('%Y-%m-%d %H %M',time.localtime(time.time()))+".png", frame)

    
    if ret==True:
        cv2.imshow('Watch Dogs', frame)
        out.write(frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    


cap.release()

cv2.destroyAllWindows()
