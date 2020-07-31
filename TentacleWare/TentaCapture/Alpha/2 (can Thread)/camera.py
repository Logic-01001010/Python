from threading import Thread, Lock
import cv2
import time

import os
import shutil

import mss
import numpy as np


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 1920, "height": 1080}

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


class CameraStream(object):
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)


        #얼굴 인식 캐스케이드 파일 읽는다
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        

        (self.grabbed, self.frame) = self.stream.read()
        

        
        self.started = False
        self.read_lock = Lock()

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        frame = img = np.array(sct.grab(monitor))
        self.read_lock.release()



        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)



        if len(faces) == True:
            # 인식된 얼굴에 사각형을 출력한다
            for (x,y,w,h) in faces:
                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                 cv2.putText(frame, text='Detected', org=(x, y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)

            # 시간 텍스트 출력
            cv2.putText(frame, text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), org=(30, 450), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)


            # capture 폴더 유무 확인
            if os.path.isdir("capture") == True:

                # capture 폴더의 용량이 정해진 값보다 큰지 같은지
                if get_dir_size('capture') >= 360000*1024:
                    shutil.rmtree("./capture")
                    os.mkdir("capture")
            else:
                os.mkdir("capture")

                
            
            # 얼굴 캡쳐 이미지 저장
            cv2.imwrite(time.strftime('capture\%Y-%m-%d %H %M',time.localtime(time.time()))+".png", frame)
            

        # 시간 표기
        cv2.putText(frame, text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), org=(30, 450), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)
        
        return frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()
