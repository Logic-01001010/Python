import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 720) # 윈도우 크기
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

count = 99

while(cap.isOpened()):
    
    if count != time.strftime('%H',time.localtime(time.time())): # 시간이 바뀌면 영상파일을 새로 만든다. (시간으로 감지)
        
        count = time.strftime('%H',time.localtime(time.time()))
        print('시간 변경 감지')
        
        out = cv2.VideoWriter(time.strftime('%Y-%m-%d %I시 %M분',time.localtime(time.time()))+'.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))

        print('파일 생성:',time.strftime('%Y-%m-%d %I시 %M분',time.localtime(time.time()))+'.avi')

    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 화면 반전 0: 상하, 1: 좌우

    # 시간 텍스트 출력
    cv2.putText(frame, text=time.strftime('%Y-%m-%d %I:%M:%S',time.localtime(time.time())), org=(30, 450), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,255,255), thickness=2)

    
    if ret==True:
        cv2.imshow('Record&Save', frame)
        out.write(frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    


cap.release()

cv2.destroyAllWindows()
